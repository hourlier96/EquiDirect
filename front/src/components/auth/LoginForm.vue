<template>
  <div class="q-pa-md" style="max-width: 400px">
    <q-form @submit="onSubmit" @reset="onReset" class="login-form q-gutter-md">
      <q-input standout v-model="email" type="email">
        <template v-slot:prepend>
          <q-icon name="mail" />
        </template>
      </q-input>

      <q-input filled type="password" v-model="password" label="Mot de passe" />

      <!-- <q-toggle v-model="accept" label="I accept the license and terms" /> -->

      <div>
        <q-btn label="Se connecter" type="submit" color="green" />
        <q-btn
          label="Réinitialiser"
          type="reset"
          color="green"
          flat
          class="q-ml-sm"
        />
      </div>
      <div>
        <router-link class="to-signup" to="/register">
          Pas encore membre? Inscrit toi ici !</router-link
        >
      </div>
      <div>
        <router-link class="to-signup" to="/forgotten-password">
          Mot de passe oublié
        </router-link>
      </div>
    </q-form>
  </div>
</template>

<script>
import { useQuasar } from "quasar";
import { ref } from "vue";
import { authStore } from "@/stores/auth";
export default {
  props: {
    register: Boolean,
  },
  setup() {
    const $q = useQuasar();
    const store = authStore();

    const email = ref(null);
    const password = ref(null);

    return {
      email,
      password,

      onSubmit() {
        if (email.value === null || password.value === null) {
          $q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "Entrez vos identifiants",
          });
        } else {
          store.storeUser(email.value).then(function () {
            if (store.currentUser.email) {
              $q.notify({
                color: "green-4",
                textColor: "white",
                icon: "cloud_done",
                message: "Rebonjour " + store.currentUser.firstname,
              });
            } else {
              $q.notify({
                color: "red-4",
                textColor: "white",
                icon: "cloud_done",
                message: "Identifiants incorrects",
              });
            }
          });
        }
      },

      onReset() {
        email.value = null;
        password.value = null;
      },
    };
  },
};
</script>

<style>
.login-form {
  text-align: center;
}

.to-signup {
  margin-top: 10px;
}
</style>
