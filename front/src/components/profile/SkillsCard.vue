<template>
  <div class="col-9">
    <div class="row q-mb-xl justify-around no-wrap">
      <h5 color="green">Compétences</h5>
      <q-input
        class="col-5 q-ml-auto"
        type="date"
        readonly
        v-model="user!.created_at"
        hint="En activité depuis le"
      ></q-input>
    </div>
    <div class="row justify-around no-wrap">
      <q-input
        class="col-5 q-mb-md"
        filled
        readonly
        v-model="user!.firstname"
        label="Prénom"
      ></q-input>
      <q-input
        class="col-5 q-mb-md"
        filled
        readonly
        v-model="user!.lastname"
        label="Nom"
      ></q-input>
    </div>
    <div class="row justify-around no-wrap">
      <q-input
        class="col-5 q-mb-md"
        filled
        readonly
        v-model="user!.email"
        label="Email"
      ></q-input>
      <q-input
        class="col-5 q-mb-md"
        filled
        readonly
        v-model="individual!.address"
        label="Addresse"
      ></q-input>
    </div>
    <div class="row justify-around no-wrap">
      <q-input
        class="col-5 q-mb-md"
        filled
        readonly
        v-model="user!.age"
        label="Date de naissance"
      ></q-input>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  user: {
    type: Object,
  },
  individual: {
    type: Object,
  },
});
</script>
