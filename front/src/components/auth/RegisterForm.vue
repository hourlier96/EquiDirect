<template>
  <CardContainer
    title="Inscription"
    :centered="true"
    :bigTitle="true"
    width="700px"
  >
    <q-form
      @submit="onSubmit"
      @reset="onReset"
      class="login-form text-center q-gutter-lg"
    >
      <q-input standout v-model="firstname" type="text" label="Prénom">
      </q-input>
      <q-input standout v-model="lastname" type="text" label="Nom"> </q-input>
      <q-input standout v-model="email" type="email" label="Email">
        <template v-slot:prepend>
          <q-icon name="mail" />
        </template>
      </q-input>

      <q-input
        filled
        type="password"
        v-model="password"
        label="Mot de passe"
        :rules="passwordRules"
      />
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
          <q-img
            class="role-img"
            src="src/assets/images/register/prestataire.jpg"
          >
            <div
              class="text-subtitle2 absolute-top text-center"
              :class="{ 'role-selected': role === 'INDIVIDUAL' }"
            >
              Un prestataire
            </div>
          </q-img>
        </q-card>

        <q-card
          class="card-company q-ma-xs col-5 cursor-pointer"
          @click="setRole('COMPANY')"
        >
          <q-img
            class="role-img"
            src="src/assets/images/register/entreprise.jpg"
          >
            <div
              class="text-subtitle2 absolute-top text-center"
              :class="{ 'role-selected': role === 'COMPANY' }"
            >
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
  </CardContainer>
</template>

<script>
import { ref } from "vue";
import router from "@/router";

import { authStore } from "@/stores/auth";
import { notify } from "@/helpers/notify";
import CardContainer from "../common/CardContainer.vue";

export default {
  props: {
    register: Boolean,
  },
  computed: {
    passwordRules() {
      return [
        (val) =>
          (val.length >= 8 && val !== val.toLowerCase()) ||
          "La taille du mot de passe doit être de 8 caractères minimum et contenir au moins une majuscule",
      ];
    },
  },
  setup() {
    const store = authStore();
    const firstname = ref(null);
    const lastname = ref(null);
    const email = ref(null);
    const password = ref(null);
    const confirm_password = ref(null);
    let role = ref(null);
    return {
      firstname,
      lastname,
      email,
      password,
      confirm_password,
      role,
      setRole(choice) {
        role.value = choice;
      },
      onSubmit() {
        if (
          firstname.value == null ||
          lastname.value == null ||
          email.value === null ||
          password.value === null ||
          role.value === null
        ) {
          notify.error("Completez entièrement le formulaire");
        } else if (password.value !== confirm_password.value) {
          notify.error("Les mots de passe ne correspondent pas");
        } else {
          store
            .signIn(
              firstname.value,
              lastname.value,
              email.value,
              password.value,
              role.value
            )
            .then((response) => {
              router.push({
                name: "verify",
                query: {
                  confirmation_id: response.data.confirmation_id,
                  email: email.value,
                },
              });
              notify.success("Inscription validée");
            })
            .catch((e) => {
              if ("response" in e) {
                if (e.response.data.detail === "Email already taken") {
                  notify.error(
                    "Cette addresse e-mail a déja été enregistrée. Veuillez en choisir une autre."
                  );
                }
              } else {
                console.error("Error on signIn:", e);
              }
            });
        }
      },
      onReset() {
        firstname.value = null;
        lastname.value = null;
        email.value = null;
        password.value = null;
        confirm_password.value = null;
        role.value = null;
      },
    };
  },
  components: { CardContainer },
};
</script>

<style>
.card-presta:hover,
.card-company:hover {
  opacity: 0.8;
}

.role-img {
  max-height: 180px;
  object-position: 50% 20% !important;
}

.role-selected {
  background: rgb(76, 175, 80, 0.8) !important;
}
</style>
