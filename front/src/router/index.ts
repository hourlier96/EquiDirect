import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import Login from "@/views/Login.vue";
import MailSending from "@/views/mailing/MailSending.vue";
import MailValidation from "@/views/mailing/MailValidation.vue";
import ProfileGlobal from "@/views/users/ProfileGlobal.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/register",
      name: "register",
      component: Login,
      props: { register: true },
    },
    {
      path: "/verify",
      name: "verify",
      component: MailSending,
    },
    {
      path: "/validate",
      name: "validate",
      component: MailValidation,
    },
    {
      path: "/login",
      name: "login",
      component: Login,
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: HomeView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/profile",
      name: "profile",
      component: ProfileGlobal,
      meta: {
        requiresAuth: true,
      },
    },
    { path: "/:catchAll(.*)", redirect: "/login" },
  ],
});

export default router;
