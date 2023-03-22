<template>
  <v-container class="fill-height">
    <game-timer class="d-flex justify-end"/>
    <v-responsive class="d-flex align-center text-center fill-height">
        <game-list/>
    </v-responsive>
  </v-container>
</template>

<script>

import GameList from "@/components/GameList.vue"
import GameTimer from "@/components/GameTimer.vue"

export default {
  name: 'HomeView',
  components: {
    GameList,
    GameTimer
  }
}
</script>
