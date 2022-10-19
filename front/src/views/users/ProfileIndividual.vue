<template>
  <CardContainer>
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
          class="q-mt-xs justify-center"
          v-model="individual!.rate"
          readonly
          style="width: 100%"
          size="2.5em"
          color="green-5"
          icon="star_border"
          icon-selected="star"
          icon-half="star_half"
        />
        <q-input
          class="q-mx-auto"
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
      <Transition mode="out-in">
        <GeneralCard
          :user="user"
          :individual="individual"
          v-if="section == 'general'"
        />
        <SkillsCard
          :user="user"
          :individual="individual"
          v-else-if="section == 'skills'"
        />
        <SearchCard
          :user="user"
          :individual="individual"
          v-else-if="section == 'search'"
        />
      </Transition>
    </div>
  </CardContainer>

  <!-- <CardContainer> {{ section }} </CardContainer> -->
  <!-- <div>
    : photo, biographie, note, nom, prénom, age, email, adresse, date de
    création du compte
  </div>
  <div>: Langues, Disciplines, Skills, Galop, Expérience, Diplômes, Autres</div>
  <div>
    : Calendrier, Distance de trajet max, autoentrepreneur, en recherche,
    Période de travail, type de travail, prix, besoin d'hébergement
  </div> -->
</template>

<script setup lang="ts">
import { authStore } from "@/stores/auth";
import { individualStore } from "@/stores/individual";
import { onMounted } from "vue";
import userAPI from "@/api/resources/users";
import individualAPI from "@/api/resources/individual";
import CardContainer from "@/components/common/CardContainer.vue";
import GeneralCard from "@/components/profile/GeneralCard.vue";
import SkillsCard from "@/components/profile/SkillsCard.vue";
import SearchCard from "@/components/profile/SearchCard.vue";

const authentStore = authStore();
const indivStore = individualStore();

const user = authentStore.currentUser;
const individual = indivStore.individual;

defineProps({
  section: String,
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

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
