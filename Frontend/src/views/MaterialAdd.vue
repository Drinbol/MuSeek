<template>
  <div class="material-add">
    <a-form :model="material" @submit="handleSubmit" layout="vertical">
      <a-form-item>
        <a-tree-select
          v-model:value="material.tag_ids"
          multiple
          tree-checkable
          placeholder="请选择标签"
          style="width: 100%"
          :tree-data="tagTreeData"
          :tree-default-expanded-keys="[]"
        ></a-tree-select>
      </a-form-item>
      <a-form-item>
        <div style="display: flex">
          <a-textarea v-model:value="material.content" :rows="4" style="flex: 1" />
        </div>
      </a-form-item>
      <a-form-item>
        <div style="text-align: center">
          <a-button type="primary" @click="pasteContent" style="margin-right: 16px">粘贴</a-button>
          <a-button type="primary" html-type="submit" style="margin-right: 16px">保存</a-button>
          <a-button @click="resetForm">清除</a-button>
        </div>
      </a-form-item>
    </a-form>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref, computed } from 'vue';
import { message } from 'ant-design-vue';
import type { Tag } from '../types';
import { createMaterial, listTags } from '../api/material';

interface TreeNode {
  key: string;
  title: string;
  value: string;
  children?: TreeNode[];
}

export default defineComponent({
  name: 'MaterialAdd',
  setup() {
    const material = ref({
      content: '',
      tag_ids: [],
    });
    const tags = ref<Tag[]>([]);

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
          key: tag.id.toString(),
          title: tag.name,
          value: tag.id.toString(),
        });
      });

      return Object.values(typeMap);
    });

    onMounted(async () => {
      tags.value = await listTags();
    });

    const handleSubmit = async () => {
      try {
        await createMaterial({
          content: material.value.content,
          tag_ids: material.value.tag_ids.map(Number),
        });
        message.success('素材创建成功');
        resetForm();
      } catch (error) {
        console.error('Failed to create material: ', error);
        message.error('素材创建失败,请重试');
      }
    };

    const resetForm = () => {
      material.value.content = '';
      material.value.tag_ids = [];
    };

    const pasteContent = async () => {
      try {
        const text = await navigator.clipboard.readText();
        material.value.content = text;
      } catch (err) {
        console.error('Failed to read clipboard contents: ', err);
      }
    };

    return {
      material,
      tags,
      tagTreeData,
      handleSubmit,
      resetForm,
      pasteContent,
    };
  },
});
</script>

<style scoped>
.material-add {
  max-width: 100%;
  margin: 0 auto;
  max-height: calc(100vh - 120px);
  min-height: calc(100vh - 120px);
  height: 100%;
}
</style>