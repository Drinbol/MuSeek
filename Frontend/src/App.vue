<script setup lang="ts">
import { ref, computed, defineComponent } from 'vue';
import MaterialDetail from './components/MaterialDetail.vue';
import MaterialEdit from './components/MaterialEdit.vue';

type TabComponent = ReturnType<typeof defineComponent>;

const tabs: Record<string, TabComponent> = {
  Tab1: MaterialDetail,
  Tab2: MaterialEdit,
  Tab3: { template: '<div>Content of Tab 3</div>' } as TabComponent
};

const currentTab = ref('Tab1');
const currentComponent = computed(() => tabs[currentTab.value]);

import type { TabsProps } from 'ant-design-vue/es/tabs';
const tabPosition = ref<TabsProps['tabPosition']>('left');
</script>

<template>
  <a-style-provider hash-priority="high">
    <a-tabs v-model:activeKey="currentTab" :tab-position="tabPosition" animated class="tabs">
      <a-tab-pane key="Tab1" tab="Tab 1">
        <component :is="currentComponent" />
      </a-tab-pane>
      <a-tab-pane key="Tab2" tab="Tab 2">
        <component :is="currentComponent" />
      </a-tab-pane>
      <a-tab-pane key="Tab3" tab="Tab 3">
        <component :is="currentComponent" />
      </a-tab-pane>
    </a-tabs>
  </a-style-provider>
</template>