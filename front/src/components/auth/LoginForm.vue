<template>
  <CardContainer
    title="Connexion"
    :centered="true"
    :bigTitle="true"
    width="700px"
  >
    <q-form
      @submit="onSubmit"
      @reset="onReset"
      class="login-form text-center q-gutter-lg"
    >
      <q-input standout v-model="email" type="email" label="Entrez votre email">
        <template v-slot:prepend>
          <q-icon name="mail" />
        </template>
      </q-input>

      <q-input
        filled
        type="password"
        v-model="password"
        label="Entrez votre mot de passe"
      />

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
        <router-link class="to-signup" to="/register"
          >Pas encore membre? Inscris toi ici !</router-link
        >
      </div>
      <div>
        <router-link class="to-signup" to="/forgotten-password">
          Mot de passe oublié
        </router-link>
      </div>
    </q-form>
  </CardContainer>
</template>

<script>
import { ref } from "vue";
import router from "@/router";

import userAPI from "@/api/resources/users";
import { authStore } from "@/stores/auth";
import { notify } from "@/helpers/notify";

import CardContainer from "../common/CardContainer.vue";
export default {
  props: {
    register: Boolean,
  },
  setup() {
    const store = authStore();

    const email = ref(null);
    const password = ref(null);
    return {
      email,
      password,

      async onSubmit() {
        if (email.value === null || password.value === null) {
          notify.warning("Entrez vos identifiants");
        } else {
          store
            .getJwt({ email: email.value, password: password.value })
            .then(async function (response) {
              const token = response.data.access_token;
              await userAPI
                .getUserFromEmail({ email: email.value, access_token: token })
                .then((response) => {
                  const user = response.data;
                  if (!user.confirmed) {
                    notify.error(
                      "Votre compte est en attente de validation. Vérifiez votre boîte mail."
                    );
                  } else {
                    store.accessToken = token;
                    store.storeUser(user);
                    notify.success("Rebonjour " + store.currentUser.firstname);
                    router.push({ path: "/dashboard" });
                  }
                })
                .catch((e) => {
                  console.error(e);
                });
            })
            .catch(() => {
              notify.error("Identifiants incorrects");
            });
        }
      },

      onReset() {
        email.value = null;
        password.value = null;
      },
    };
  },
  components: { CardContainer },
};
</script>
