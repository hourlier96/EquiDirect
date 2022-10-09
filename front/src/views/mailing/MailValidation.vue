<template>
  <main>
    <div
      v-if="validation === true"
      class="q-mx-auto q-my-auto text-center"
      style="max-width: 900px"
    >
      <q-banner inline-actions rounded class="bg-green text-white">
        Votre addresse email a été vérifié ! Vous pouvez désormais vous
        connecter avec vos identifants.
        <br />
        <br />
        <router-link class="to-signup text-black" to="/login">
          Cliquez ici pour vous connecter
        </router-link>
      </q-banner>
    </div>
    <div
      v-if="validation === false"
      class="q-mx-auto q-my-auto text-center"
      style="max-width: 900px"
    >
      <q-banner inline-actions rounded class="bg-red text-white">
        Une erreur est survenue lors de la validation de votre compte.
        <br />
        <br />
        <router-link
          class="to-signup text-black"
          :to="`/verify?confirmation_id=${confirmation_id}&email=${email}`"
        >
          Cliquez ici pour recevoir un nouveau mail
        </router-link>
      </q-banner>
    </div>
  </main>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

import userAPI from "@/api/resources/users";
export default {
  setup() {
    const route = useRoute();

    let validation = ref(null);

    onMounted(async () => {
      await userAPI
        .getUserFromEmailAndConfirmId({
          email: route.query.email,
          confirmation_id: route.query.confirmation_id,
          access_token: route.query.access_token,
        })
        .then(async (response) => {
          const userId = response.data.id;
          await userAPI
            .confirmUser(userId, { confirmed: true }, route.query.access_token)
            .then(() => {
              validation.value = true;
            })
            .catch((e) => {
              validation.value = false;
              console.error(e);
            });
        })
        .catch((e) => {
          validation.value = false;
          console.error(e);
        });
    });
    return {
      confirmation_id: route.query.confirmation_id,
      email: route.query.email,
      access_token: route.query.access_token,
      validation,
    };
  },
};
</script>
