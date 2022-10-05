<template>
  <div class="wrapper fixed-top">
    <div class="title q-pa-md">
      <h3 class="text-green">EQUISPHERE</h3>
    </div>
    <div v-if="session.isConnected()" class="navbar q-pa-md">
      <q-btn class="q-ml-md text-green" push flat label="Contact"> </q-btn>
      <q-btn class="q-ml-md text-green" push flat label="Qui sommes nous?">
      </q-btn>
      <q-btn class="nav-item text-green" flat label="Profil"></q-btn>
      <q-separator class="separator q-ml-xs" vertical />
      <q-avatar class="q-ml-lg pic-profil" size="50px">
        <img src="https://cdn.quasar.dev/img/avatar4.jpg" />
      </q-avatar>
      <q-btn round class="q-ml-md text-green">
        <q-icon size="2em" name="mail"></q-icon>
      </q-btn>
      <q-btn round class="q-ml-xl text-green">
        <q-icon @click.prevent="logout()" size="2em" name="logout"></q-icon
      ></q-btn>
    </div>
  </div>
</template>

<script lang="ts">
import { session } from "@/helpers/session";
import router from "@/router";
import { authStore } from "@/stores/auth";
export default {
  setup() {
    const store = authStore();
    return {
      session,

      logout() {
        console.log(store.currentUser);
        store.resetUser();
        console.log(store.currentUser);
        router.push({ path: "/login" });
      },
    };
  },
};
</script>

<style>
.wrapper {
  display: flex;
  text-align: end;
  border-bottom: solid 1px;
  justify-content: space-between;
  align-items: flex-end;
  padding: 0rem 2rem 0rem 2rem;
  background: azure;
  z-index: 1000;
}

.navbar span {
  font-weight: bold;
}

.separator {
  display: inline-block;
  height: 40px;
  vertical-align: top;
}
</style>
