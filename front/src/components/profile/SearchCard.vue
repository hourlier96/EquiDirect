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
      text: "search",
    };
  },
};
</script>
