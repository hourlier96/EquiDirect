import { authStore } from "@/stores/auth";

export const session = {
    isConnected() {
        return authStore().currentUser.email != undefined && authStore().currentUser.email != null
    },
    getFirstName() {
        return authStore().currentUser.firstname
    },
    getLastName() {
        return authStore().currentUser.lastname
    },
    getRole() {
        return authStore().currentUser.role || ""
    },
    getEmail() {
        return authStore().currentUser.email
    },
    getId() {
        return authStore().currentUser.id
    }
}