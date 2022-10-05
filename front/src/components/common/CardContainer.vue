<template>
  <div class="container q-pa-md" :style="'max-width:' + width">
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  width: String,
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
