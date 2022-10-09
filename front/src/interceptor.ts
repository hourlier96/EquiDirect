import axiosInstance from "./helpers/axios";
import { session } from "./helpers/session";
import { authStore } from "./stores/auth";
import router from "@/router/index";
const setup = () => {
  router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
      if (!session.isConnected()) {
        // Auth required, not connected
        next({ name: 'login' })
      } else {
        // Auth required, already connected
        next()
      }
    } else if (session.isConnected()) {
      // Not auth required, already connected
      next({ name: 'dashboard' })
    } else {
      // Not auth required, not connected
      next() 
    }
  })

  axiosInstance.axiosInstance.interceptors.request.use(
    (config) => {
      const store = authStore();
      // Send Bearer when user is connected
      if (store.accessToken) {
        const token = store.accessToken;
        if (config.headers) {
          config.headers["Authorization"] = `Bearer ${token}`;
          return config;
        }
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
};

export default setup;
