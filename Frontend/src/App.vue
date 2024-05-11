<template>
  <a-style-provider hash-priority="high">
    <a-layout>
      <a-layout-sider
        v-if="!isMobile"
        :style="{
          overflow: 'auto',
          height: '100vh',
          position: 'fixed',
          left: 0,
          top: 0,
          bottom: 0,
        }"
        width="150"
      >
        <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
          <a-menu-item key="1">
          <router-link to="/">
            <user-outlined />
            <span class="nav-text">素材</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="2">
          <router-link to="/MaterialAdd">
            <video-camera-outlined />
            <span class="nav-text">添加</span>
          </router-link>
        </a-menu-item>
        </a-menu>
      </a-layout-sider>

      <a-layout :style="{ marginLeft: isMobile ? '0' : '150px' }">
        <a-layout-header 
        v-if="isMobile"
        >
          <a-menu
              v-model:selectedKeys="selectedKeys"
              theme="dark"
              mode="horizontal"
              :style="{ lineHeight: '64px' }"
          >
          <a-menu-item key="1">
            <router-link to="/">
              <user-outlined />
              <span class="nav-text">素材</span>
            </router-link>
          </a-menu-item>
          <a-menu-item key="2">
            <router-link to="/MaterialAdd">
              <video-camera-outlined />
              <span class="nav-text">添加</span>
            </router-link>
          </a-menu-item>
          </a-menu>
        </a-layout-header>

        <a-layout-content :style="{ overflow: 'hiden', background: '#FFF'}">
          <router-view></router-view>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-style-provider>
</template>


<script lang="ts" setup>
import { ref, onMounted, onUnmounted } from 'vue';
const selectedKeys = ref<string[]>(['1']);
const isMobile = ref<boolean>(false);

const handleResize = () => {
  isMobile.value = window.innerWidth < 768;
};

onMounted(() => {
  handleResize();
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
});
</script>

<style scoped> /* scoped表示该样式只在当前组件生效 */

.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #ffffff33;
}

</style>
