<script setup lang="ts">
import CardContainer from "@/components/common/CardContainer.vue";
import GeneralCard from "@/components/profile/GeneralCard.vue";
import SkillsCard from "@/components/profile/SkillsCard.vue";
import SearchCard from "@/components/profile/SearchCard.vue";

defineProps({
  section: String,
});
</script>

<template>
  <CardContainer title="Entrez vos informations">
    <Transition mode="out-in">
      <GeneralCard v-if="section == 'general'" />
      <SkillsCard v-else-if="section == 'skills'" />
      <SearchCard v-else-if="section == 'search'" />
    </Transition>
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
