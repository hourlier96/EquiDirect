import { Notify } from 'quasar'

export const notify = {
    success(message, icon="cloud_done") {
        Notify.create({
            color: "green-4",
            textColor: "white",
            icon: icon,
            message: message,
        })
    },
    warning(message, icon="cloud_off") {
        Notify.create({
            color: "orange",
            textColor: "white",
            icon: icon,
            message: message,
        })
    },
    error(message, icon="cloud_off") {
        Notify.create({
            color: "red-5",
            textColor: "white",
            icon: icon,
            message: message,
        })
    }
}