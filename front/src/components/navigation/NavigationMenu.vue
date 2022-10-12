<template>
  <div class="wrapper fixed-top">
    <img
      class="logo"
      src="@/assets/images/logo.png"
      alt="Equisphere"
      height="100"
    />
    <div v-if="session.isConnected()" class="navbar q-pa-md">
      <q-btn
        to="/dashboard"
        class="q-mr-auto"
        :class="isActive('dashboard')"
        flat
        color="green"
        label="Accueil"
      >
      </q-btn>
      <q-separator class="separator q-ml-lg" vertical />
      <q-avatar class="q-ml-lg pic-profil" size="50px">
        <img src="https://cdn.quasar.dev/img/avatar4.jpg" />
      </q-avatar>

      <q-btn
        :to="getProfilePage()"
        class="q-ml-md text-green"
        :class="isActive('profile')"
        round
        push
      >
        <q-icon size="2em" name="manage_accounts"></q-icon>
      </q-btn>

      <q-btn class="q-ml-md text-green" round push>
        <q-icon size="2em" name="mail"></q-icon>
      </q-btn>
      <q-btn class="q-ml-xl text-green" round push>
        <q-icon @click.prevent="logout()" size="2em" name="logout"></q-icon>
      </q-btn>
    </div>
  </div>
</template>

<script lang="ts">
import { session } from "@/helpers/session";
import router from "@/router";
import { authStore } from "@/stores/auth";
export default {
  methods: {
    isActive(name) {
      if (this.$route.matched.length > 0) {
        return { active: this.$route.matched[0].name === name };
      }
      return { active: false };
    },
    getProfilePage() {
      return `/profile/${session.getId()}/${session
        .getRole()
        .toLowerCase()}?view=general`;
    },
  },
  setup() {
    const store = authStore();
    return {
      session,
      logout() {
        store.resetUser();
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
  box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset,
    rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
  border: 1px solid rgb(201, 201, 201);
  width: 93%;
  border-radius: 0px 0px 10px 10px;
  margin: auto;
  justify-content: space-between;
  align-items: flex-end;
  padding: 0rem 2rem 0rem 2rem;
  background: #f8fffe;
  z-index: 1000;
}

.navbar span {
  font-weight: bold;
}

.wrapper .active {
  color: white !important;
  background-color: var(--vt-c-green) !important;
}

.separator {
  display: inline-block;
  height: 50px;
  vertical-align: top;
  width: 1px;
}
</style>
