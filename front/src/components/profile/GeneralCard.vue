<template>
  <div>
    <div class="row">
      <div class="col-2">
        <q-avatar
          rounded
          class="q-mx-auto pic-profil"
          size="110px"
          style="display: block"
        >
          <img src="https://cdn.quasar.dev/img/avatar4.jpg" />
        </q-avatar>
        <q-badge
          style="position: absolute; top: -5px; left: 45px"
          class="q-mx-auto"
          color="green"
        >
          {{ roleLabel(user!.role) }}
        </q-badge>
        <q-btn
          class="q-mx-auto"
          color="green"
          fab-mini
          size="xs"
          icon="upload"
          style="position: absolute; top: -5px; right: 45px"
        >
        </q-btn>
      </div>

      <div class="col-1">
        <q-separator
          class="q-mx-auto"
          style="height: 100%"
          size="1px"
          :vertical="true"
        ></q-separator>
      </div>

      <div class="col-9">
        <div class="row justify-around no-wrap">
          <q-input
            class="col-5 q-mb-md"
            filled
            v-model="user!.firstname"
            label="Prénom"
          ></q-input>
          <q-input
            class="col-5 q-mb-md"
            filled
            v-model="user!.lastname"
            label="Nom"
          ></q-input>
        </div>
        <div class="row justify-around no-wrap">
          <q-input
            class="col-5 q-mb-md"
            filled
            v-model="user!.email"
            label="Email"
          ></q-input>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import userAPI from "@/api/resources/users";
import individualAPI from "@/api/resources/individual";
import { authStore } from "@/stores/auth";
import { individualStore } from "@/stores/individual";

const store = authStore();
const indivStore = individualStore();

const props = defineProps({
  user: {
    type: Object,
  },
  individual: {
    type: Object,
  },
});

onMounted(async () => {
  getUser();
  getIndividual();
});

async function getUser() {
  await userAPI
    .getUserFromEmail({ email: store.currentUser.email })
    .then(async (response) => {
      const user = response.data;
      store.storeUser(user);
    });
}

async function getIndividual() {
  await individualAPI
    .getIndividualFromUser({ user_id: store.currentUser.id })
    .then((response) => {
      const individual = response.data;
      individualStore().storeIndividual(individual);
    });
}

function roleLabel(role) {
  return role === "COMPANY" ? "Entreprise" : "Prestataire";
}
</script>
