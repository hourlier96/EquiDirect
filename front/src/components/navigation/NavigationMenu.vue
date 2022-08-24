<template>
  <div class="wrapper">
    <div class="title q-pa-md"><h3>EQUISPHERE</h3></div>
    <div class="navbar q-pa-md">
      <q-btn class="nav-item" push flat color="green" label="Contact"> </q-btn>
      <q-btn class="nav-item" push flat color="green" label="Qui sommes nous?">
      </q-btn>
      <q-btn class="nav-item" flat color="green" label="Profil"></q-btn>
      <q-separator class="separator nav-item" vertical />
      <q-icon class="nav-item" size="2em" name="mail"></q-icon>
      <q-avatar class="nav-item pic-profil" size="50px">
        <img src="https://cdn.quasar.dev/img/avatar4.jpg" />
      </q-avatar>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import UsersAPI from "@/api/resources/users.js";
import { RouterLink } from "vue-router";

onMounted(() => {
  UsersAPI.index();
});
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

.nav-item {
  margin-left: 15px;
}

.separator {
  display: inline-block;
  height: 40px;
  vertical-align: top;
}
</style>
