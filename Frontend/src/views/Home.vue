<template>
    <a-layout>
      <a-layout-sider width="150" style="background: #fff">
        <a-menu mode="inline" :default-selected-keys="['1']" :style="{ height: '100%', borderRight: 0 }">
          <a-menu-item key="1">人物</a-menu-item>
          <a-menu-item key="2">场景</a-menu-item>
          <a-menu-item key="3">物品</a-menu-item>
          <a-menu-item key="4">事件</a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout style="padding: 0 24px 24px">
        <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }">
          <a-list item-layout="horizontal" :data-source="materials">
            <template #renderItem="{ item }">
              <a-list-item>
                <a-list-item-meta :description="item.content">
                  <template #title>
                    <router-link :to="'/materials/' + item.id">{{ item.content.slice(0, 20) }}</router-link>
                  </template>
                  <template #avatar>
                    <a-avatar src="https://joeschmoe.io/api/v1/random" />
                  </template>
                </a-list-item-meta>
              </a-list-item>
            </template>
          </a-list>
          <a-form :model="newMaterial" layout="inline" @submit="handleSubmit">
            <a-form-item label="内容">
              <a-input v-model:value="newMaterial.content" />
            </a-form-item>
            <a-form-item label="标签">
              <a-select v-model:value="newMaterial.tags" mode="multiple" style="width: 100%">
                <a-select-option v-for="tag in tags" :key="tag.id" :value="tag.id">
                  {{ tag.name }}
                </a-select-option>
              </a-select>
            </a-form-item>
            <a-form-item>
              <a-button type="primary" html-type="submit">添加</a-button>
            </a-form-item>
          </a-form>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </template>
  
  <script lang="ts">
  import { defineComponent, onMounted, ref } from 'vue';
  import type { Material, Tag } from '@/types';
  import { listMaterials, listTags } from '@/api/material';
  
  export default defineComponent({
    name: 'Home',
    setup() {
      const materials = ref<Material[]>([]);
      const tags = ref<Tag[]>([]);
      const newMaterial = ref<Partial<Material>>({
        content: '',
        tags: []
      });
  
      onMounted(async () => {
        materials.value = await listMaterials();
        tags.value = await listTags();
      });
  
      const handleSubmit = async () => {
        // TODO: 调用创建素材的API
        newMaterial.value = {
          content: '',
          tags: []
        };
      };
  
      return {
        materials,
        tags,
        newMaterial,
        handleSubmit
      };
    }
  });
  </script>