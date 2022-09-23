<template>
  <div class="q-pa-md" style="max-width: 700px">
    <q-form @submit="onSubmit" @reset="onReset" class="login-form q-gutter-md">
      <q-input standout v-model="firstname" type="text" label="Prénom">
      </q-input>
      <q-input standout v-model="lastname" type="text" label="Nom"> </q-input>
      <q-input standout v-model="email" type="email" label="Email">
        <template v-slot:prepend>
          <q-icon name="mail" />
        </template>
      </q-input>

      <q-input filled type="password" v-model="password" label="Mot de passe" />
      <q-input
        class="q-mb-md"
        filled
        type="password"
        v-model="confirm_password"
        label="Confirmer mot de passe"
      />
      <span class="text-green-4 text-bold">Je suis...</span>
      <div class="row justify-center">
        <q-card
          class="card-presta q-ma-xs col-5 cursor-pointer"
          @click="setRole('INDIVIDUAL')"
        >
          <q-img src="https://cdn.quasar.dev/img/parallax2.jpg">
            <div class="text-subtitle2 absolute-top text-center">
              Un prestataire
            </div>
          </q-img>
        </q-card>

        <q-card
          class="card-company q-ma-xs col-5 cursor-pointer"
          @click="setRole('COMPANY')"
        >
          <q-img src="https://cdn.quasar.dev/img/parallax2.jpg">
            <div class="text-subtitle2 absolute-top text-center">
              Une entreprise
            </div>
          </q-img>
        </q-card>
      </div>

      <!-- <q-toggle v-model="accept" label="I accept the license and terms" /> -->

      <div>
        <q-btn label="Je m'inscris" type="submit" color="green" />
        <q-btn
          label="Réinitialiser"
          type="reset"
          color="green"
          flat
          class="q-ml-sm"
        />
      </div>
      <div>
        <router-link class="to-signup q-mt-xs" to="/login">
          Déja membre? Connecte toi ici !</router-link
        >
      </div>
    </q-form>
  </div>
</template>

<script>
import { ref } from "vue";
import { authStore } from "@/stores/auth";
import { notify } from "@/helpers/notify";
export default {
  props: {
    register: Boolean,
  },
  setup() {
    const store = authStore();
    const firstname = ref(null);
    const lastname = ref(null);
    const email = ref(null);
    const password = ref(null);
    const confirm_password = ref(null);
    let role = null;
    return {
      firstname,
      lastname,
      email,
      password,
      confirm_password,
      role,

      setRole(choice) {
        role = choice;
      },

      onSubmit() {
        if (
          firstname.value == null ||
          lastname.value == null ||
          email.value === null ||
          password.value === null
        ) {
          notify.error("Completez entièle formulaire");
        } else if (password.value !== confirm_password.value) {
          notify.error("Les mots de passe ne correspondent pas");
        } else {
          notify.success("Connexion en cours...");
          store
            .signIn(
              firstname.value,
              lastname.value,
              email.value,
              password.value,
              role
            )
            .then(function () {
              // if (store.currentUser.email) {
              //   notify.success("Rebonjour " + store.currentUser.firstname);
              // } else {
              //   notify.error("Identifiants incorrects");
              // }
            });
        }
      },

      onReset() {
        firstname.value = null;
        lastname.value = null;
        email.value = null;
        password.value = null;
        role = null;
      },
    };
  },
};
</script>

<style>
.login-form {
  text-align: center;
}

.card-presta:hover,
.card-company:hover {
  opacity: 0.8;
}
</style>
