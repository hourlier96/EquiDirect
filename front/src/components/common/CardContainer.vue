<template>
  <div class="container q-pa-md" :style="'width:' + width">
    <h5
      v-if="title"
      class="q-mb-xl text-green"
      :class="{ 'text-center': bigTitle, 'text-bold': bigTitle }"
    >
      {{ title }}
    </h5>
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  width: String,
  title: String,
  bigTitle: Boolean,
});
</script>

<style>
.container {
  border-radius: 10px;
  background-color: rgb(247, 245, 245);
  box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px,
    rgba(0, 0, 0, 0.22) 0px 15px 12px;
}
</style>
