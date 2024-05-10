<template>
  <div class="material-add">
    <a-form :model="material" @submit="handleSubmit">
      <a-form-item label="内容">
        <a-input v-model:value="material.content" />
      </a-form-item>
      <a-form-item label="标签">
        <a-select v-model:value="material.tag_ids" mode="multiple" style="width: 100%">
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
import { useRouter } from 'vue-router';
import type { Tag } from '@/types';
import { createMaterial, listTags } from '@/api/material';

export default defineComponent({
  name: 'MaterialEdit',
  setup() {
    const router = useRouter();
    const material = ref({
      content: '',
      tag_ids: [],
    });
    const tags = ref<Tag[]>([]);

    onMounted(async () => {
      tags.value = await listTags();
    });

    const handleSubmit = async () => {
      const newMaterial = await createMaterial({
        content: material.value.content,
        tag_ids: material.value.tag_ids,
      });
      router.push('/materials/' + newMaterial.id);
    };

    return {
      material,
      tags,
      handleSubmit,
    };
  },
});
</script>