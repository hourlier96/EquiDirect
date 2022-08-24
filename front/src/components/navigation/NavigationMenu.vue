<template>
  <div class="wrapper">
    <div class="title q-pa-md"><h3>EQUISPHERE</h3></div>
    <div class="navbar q-pa-md">
      <q-btn push flat color="green" label="Contact"> </q-btn>
      <q-btn push flat color="green" label="Qui sommes nous?"> </q-btn>

      <AccountSettingsTab />
    </div>
  </div>
</template>

<script setup lang="ts">
import AccountSettingsTab from "./AccountSettingsTab.vue";
import { RouterLink } from "vue-router";
</script>

<style>
.wrapper {
  display: flex;
  text-align: end;
  border-bottom: solid black 2px;
  margin-bottom: 1rem;
  justify-content: space-between;
  align-items: flex-end;
  padding: 0rem 2rem 0rem 2rem;
  background: linear-gradient(to right, azure, white);
}

.navbar span {
  font-weight: bold;
}
</style>
