<template>
  <div>
    <div class="row justify-around no-wrap">
      <q-input
        class="col-5 q-mb-md"
        filled
        v-model="text"
        label="Label"
        :dense="false"
      ></q-input>
      <q-input
        class="col-5 q-mb-md"
        filled
        v-model="text"
        label="Label"
        :dense="false"
      ></q-input>
    </div>
    <div class="row justify-around no-wrap">
      <q-input
        class="col-5 q-mb-md"
        filled
        v-model="text"
        label="Label"
        :dense="false"
      ></q-input>
      <q-input
        class="col-5 q-mb-md"
        filled
        v-model="text"
        label="Label"
        :dense="false"
      ></q-input>
    </div>
    <div class="row justify-around no-wrap">
      <q-input
        class="col-5 q-mb-md"
        filled
        v-model="text"
        label="Label"
        :dense="false"
      ></q-input>
      <q-input
        class="col-5 q-mb-md"
        filled
        v-model="text"
        label="Label"
        :dense="false"
      ></q-input>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      text: "skills",
    };
  },
};
</script>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.8s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
