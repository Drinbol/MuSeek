<template>
  <a-style-provider hash-priority="high">
    <a-tabs v-model:activeKey="currentTab" :tab-position="tabPosition" animated class="tabs">
      <a-tab-pane key="all" tab="全部">
        <div class="tag-selector">
          <a-tree-select
            v-model:value="selectedTags"
            multiple
            tree-checkable
            placeholder="请选择标签"
            style="width: 100%"
            :tree-data="tagTreeData"
            :tree-default-expanded-keys="[]"
          ></a-tree-select>
        </div>
        <div class="table-container">
          <a-table 
          :columns="columns" 
          :dataSource="filteredMaterials" 
          rowKey="id" :pagination="false"
          :customRow="customRow"
          showHeader=false
          />
        </div>
      </a-tab-pane>
      <a-tab-pane v-for="tab in tabs" :key="tab.key" :tab="tab.name">
        <div class="tag-selector">
          <a-tree-select
            v-model:value="selectedTags"
            multiple
            tree-checkable
            placeholder="请选择标签"
            style="width: 100%"
            :tree-data="tagTreeData"
            :tree-default-expanded-keys="[]"
          ></a-tree-select>
        </div>
        <div class="table-container">
          <a-table 
          :columns="columns" 
          :dataSource="filteredMaterialsByTab(tab.key)" rowKey="id" :pagination="false" 
          :customRow="customRow"
          showHeader=false
          />
        </div>
      </a-tab-pane>
    </a-tabs>
  </a-style-provider>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { listMaterials, listTags } from '../api/material';
import type { Material, Tag } from '../types';
import type { TabsProps } from 'ant-design-vue';
import { message } from 'ant-design-vue';
import * as clipboard from "clipboard-polyfill";

const materials = ref<Material[]>([]);
const tags = ref<Tag[]>([]);
const currentTab = ref('all');
const selectedTags = ref<string[]>([]);
const tabPosition = ref<TabsProps['tabPosition']>('right');
const lastTapTime = ref(0);

const tabs = [
  { name: 'Tag1', key: 'Tag1' },
  { name: 'Tag2', key: 'Tag2' },
  { name: 'Tag2', key: 'Tag2' },
];

interface TreeNode {
  key: string;
  title: string;
  value: string;
  children?: TreeNode[];
}

const tagTreeData = computed<TreeNode[]>(() => {
  const typeMap: Record<string, TreeNode> = {};

  tags.value.forEach((tag) => {
    if (!typeMap[tag.type]) {
      typeMap[tag.type] = {
        key: tag.type,
        title: tag.type,
        value: tag.type,
        children: [],
      };
    }

    typeMap[tag.type].children!.push({
      key: tag.name,
      title: tag.name,
      value: tag.name,
    });
  });

  return Object.values(typeMap);
});

const filteredMaterials = computed(() => {
  if (selectedTags.value.length === 0) {
    return materials.value;
  }

  return materials.value.filter((material) => {
    const tagNames = material.tags.map((tag:Tag) => tag.name);
    const tagTypes = Array.from(new Set(material.tags.map((tag) => tag.type)));
    return selectedTags.value.every((tag) => tagNames.includes(tag) || tagTypes.includes(tag));
  });
});

const filteredMaterialsByTab = (tabKey: string) => {
  const tabTag = tabKey;
  if (selectedTags.value.length === 0) {
    return materials.value.filter((material) => material.tags.some((tag) => tag.name === tabTag));
  }

  return materials.value.filter((material) => {
    const tagNames = material.tags.map((tag) => tag.name);
    const tagTypes = Array.from(new Set(material.tags.map((tag) => tag.type)));
    return (
      selectedTags.value.every((tag) => tagNames.includes(tag) || tagTypes.includes(tag)) &&
      material.tags.some((tag) => tag.name === tabTag)
    );
  });
};


const handleDoubleClick = (record: Material) => {
  const now = Date.now();
  if (now - lastTapTime.value < 300) { // 检查两次点击的时间是否小于300毫秒
    clipboard.writeText(record.content).then(
      () => {
        message.success('内容已复制到手机剪贴板');
      },
      () => {
        message.error('内容复制失败');
      }
    );
  }
  lastTapTime.value = now; // 更新最后一次点击时间
};

const customRow = (record: Material) => {
  return {
    onDblclick: () => {
      clipboard.writeText(record.content).then(
      () => { console.log("success!"); 
        message.success('内容已复制到电脑剪贴板');
      },
      () => { console.log("error!"); 
      message.success('内容复制失败');
      }
    );
      // message.success('内容已复制到剪贴板');
    },
    onTouchend: () => handleDoubleClick(record)
  };
};


const columns = [
  {
    title: '',
    dataIndex: 'content',
    key: 'content',
  },
];

onMounted(async () => {
  materials.value = await listMaterials();
  tags.value = await listTags();
});
</script>

<style scoped>
.tag-selector {
  margin-bottom: 16px;
}

.tabs {
  height: 100%;
}

.table-container {
  max-height: 100vh;
  min-height: 100vh;
  height: 100%;
  overflow: auto;
}

.ant-tabs-tabpane {
  padding-right: 0px !important;
}
:deep(.ant-table-thead) {
  display: none;
  height: 0px;
}


:deep(.ant-table-cell) {
  font-size: 20px; 
}

/* 针对手机设备的样式 */
@media screen and (max-width: 768px) {
  :deep(.ant-tabs-nav) {
    width: 40px;
  }
  
  :deep(.ant-tabs-tab) {
    padding: 8px 3px !important;
    font-size: 12px !important;
  }

  :deep(.table-container) {
  max-height: calc(100vh - 120px);
  min-height: calc(100vh - 120px);
  height: 100%;
  overflow: auto;
  }
}
</style>