<template>
  <div>
    <a-table :columns="columns" :dataSource="materials" rowKey="id" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, h } from 'vue';
import { listMaterials } from '@/api/material';
import type { Material, Tag } from '@/types';

export default defineComponent({
  name: 'MaterialDetail',
  setup() {
    const materials = ref<Material[]>([]);

    const columns = [
      {
        title: '内容',
        dataIndex: 'content',
        key: 'content',
      },
      {
        title: '标签',
        width: '10%',
        key: 'tags',
        dataIndex: 'tags',
        customRender: ({ text: tags }: { text: Tag[] }) => tags.map((tag) => h('a-tag', { key: tag.id }, tag.name)),
      },
    ];

    onMounted(async () => {
      materials.value = await listMaterials();
    });

    return {
      materials,
      columns,
    };
  },
});
</script>