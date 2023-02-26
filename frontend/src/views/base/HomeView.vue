<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
        <game-list/>
    </v-responsive>
  </v-container>
</template>

<script>
import GameForm from "@/components/GameForm.vue"
import GameList from "@/components/GameList.vue"
import { useAppStore } from "@/stores/appStore"

export default {
  name: 'HomeView',
  components: {
    GameForm,
    GameList,
  },
}
</script>
