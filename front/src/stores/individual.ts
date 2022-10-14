import { defineStore } from "pinia";
import individualAPI from "@/api/resources/individual";

const defaultIndividual = {
  id: null,
  user_id: null,
  address: null,
  disciplines: [],
  experience: null,
  galop: null,
  housingNeed: null,
  license :null,
  maxMoveKm: null,
  prices: null,
  professionnalCard: null,
  profilPicture: null,
  rate: null,
  searchingWork: null,
  selfEmployed: null,
  skills: [],
  userId: null,
  workTime: null,
  workType: []
}

export const individualStore = defineStore({
  id: "individual",
  state: () => ({
    individual: {
      id: null,
      user_id: null,
      address: null,
      disciplines: [],
      experience: null,
      galop: null,
      housingNeed: null,
      license :null,
      maxMoveKm: null,
      prices: null,
      professionnalCard: null,
      profilPicture: null,
      rate: null,
      searchingWork: null,
      selfEmployed: null,
      skills: [],
      userId:  null,
      workTime: null,
      workType: []
    },
  }),
  getters: {
    id: (state) => state.individual.id,
    userId: (state) => state.individual.user_id,
  },
  actions: {
    storeIndividual(individual) {
      this.individual = individual
    }
  },
  persist: true
});

export default defaultIndividual;