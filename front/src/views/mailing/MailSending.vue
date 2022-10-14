<template>
  <main>
    <div
      v-if="emailSend === true"
      class="q-mx-auto q-my-auto text-center"
      style="max-width: 700px"
    >
      <q-banner inline-actions rounded class="bg-green text-white">
        Merci de vous être inscrit sur Equisphere !
        <br />
        <br />
        <div>
          Un mail vous a été envoyé à l'adresse <b> {{ email }} </b> afin de la
          vérifier. Vous pourrez ensuite vous connecter.
        </div>
      </q-banner>
    </div>

    <div
      v-if="emailSend === false"
      class="q-mx-auto q-my-auto text-center"
      style="max-width: 700px"
    >
      <q-banner inline-actions rounded class="bg-red text-white">
        L'email de confirmation n'a pas pu être envoyé !
        <br />
        <br />
        <p class="text-caption">
          Si vous avez reçu un mail dans les 15 dernières minutes, cliquez sur
          le lien dans son contenu pour valider votre addresse e-mail.
        </p>
      </q-banner>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

import mailAPI from "@/api/mail";
const route = useRoute();
const router = useRouter();

let email = route.query.email;
let emailSend = ref();

onMounted(async () => {
  if (!route.query.confirmation_id || !route.query.email) {
    router.push({ path: "/login" });
  }
  await mailAPI
    .sendVerificationMail([route.query.email], route.query.confirmation_id)
    .then(() => {
      emailSend.value = true;
    })
    .catch((e) => {
      emailSend.value = false;
    });
});
</script>
