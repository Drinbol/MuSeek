<template>
    <div class="tab">
      Posts component
    </div>
  </template>

<script setup lang="ts">
import { defineComponent } from 'vue';

const MaterialDetail = defineComponent({});

type MaterialDetailType = typeof MaterialDetail;

defineExpose<MaterialDetailType>(MaterialDetail);
</script>