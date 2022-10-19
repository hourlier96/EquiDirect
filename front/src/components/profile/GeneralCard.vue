<template>
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
      <q-rating
        class="q-mx-auto"
        v-model="individual!.rating"
        readonly
        size="2.5em"
        color="green-5"
        icon="star_border"
        icon-selected="star"
        icon-half="star_half"
      />
      <q-input
        v-model="individual!.biography"
        type="textarea"
        label="A propos de moi"
      />
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
      <div class="row q-mb-xl justify-around no-wrap">
        <h5 color="green">Informations personnelles</h5>
        <q-input
          class="col-5 q-ml-auto"
          type="date"
          readonly
          v-model="user!.created_at"
          hint="En activité depuis le"
        ></q-input>
      </div>
      <div class="row justify-around no-wrap">
        <q-input
          class="col-5 q-mb-md"
          filled
          readonly
          v-model="user!.firstname"
          label="Prénom"
        ></q-input>
        <q-input
          class="col-5 q-mb-md"
          filled
          readonly
          v-model="user!.lastname"
          label="Nom"
        ></q-input>
      </div>
      <div class="row justify-around no-wrap">
        <q-input
          class="col-5 q-mb-md"
          filled
          readonly
          v-model="user!.email"
          label="Email"
        ></q-input>
        <q-input
          class="col-5 q-mb-md"
          filled
          readonly
          v-model="individual!.address"
          label="Addresse"
        ></q-input>
      </div>
      <div class="row justify-around no-wrap">
        <q-input
          class="col-5 q-mb-md"
          filled
          readonly
          v-model="user!.age"
          label="Date de naissance"
        ></q-input>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import userAPI from "@/api/resources/users";
import individualAPI from "@/api/resources/individual";
import { authStore } from "@/stores/auth";
import { individualStore } from "@/stores/individual";

const authentStore = authStore();
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
    .getUserFromEmail({ email: authentStore.currentUser.email })
    .then(async (response) => {
      const user = response.data;
      authentStore.storeUser(user);
    });
}

async function getIndividual() {
  await individualAPI
    .getIndividualFromUser({ user_id: authentStore.currentUser.id })
    .then((response) => {
      const individual = response.data;
      indivStore.storeIndividual(individual);
    });
}

function roleLabel(role) {
  return role === "COMPANY" ? "Entreprise" : "Prestataire";
}
</script>
