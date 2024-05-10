<template>
    <div class="material-edit">
      <a-form :model="material" @submit="handleSubmit">
        <a-form-item label="内容">
          <a-input v-model:value="material.content" />
        </a-form-item>
        <a-form-item label="标签">
          <a-select v-model:value="material.tags" mode="multiple" style="width: 100%">
            <a-select-option v-for="tag in tags" :key="tag.id" :value="tag.id">
              {{ tag.name }}
            </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit">保存</a-button>
        </a-form-item>
      </a-form>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, onMounted, ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import type { Material, Tag } from '@/types';
  import { getMaterial, updateMaterial, listTags } from '@/api/material';
  
  export default defineComponent({
    name: 'MaterialEdit',
    setup() {
      const route = useRoute();
      const router = useRouter();
      const materialId = Number(route.params.id);
      const material = ref<Material>({} as Material);
      const tags = ref<Tag[]>([]);
  
      onMounted(async () => {
        material.value = await getMaterial(materialId);
        // material.value.tags = material.value.tags.map(tag => tag.id);
        tags.value = await listTags();
      });
  
      const handleSubmit = async () => {
        await updateMaterial(materialId, {
          content: material.value.content,
          tags: material.value.tags
        });
        router.push('/materials/' + materialId);
      };
  
      return {
        material,
        tags,
        handleSubmit
      };
    }
  });
  </script>