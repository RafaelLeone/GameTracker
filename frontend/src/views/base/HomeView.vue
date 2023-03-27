<template>
  <v-container class="fill-height">
    <game-timer :umJogoFoiAtualizado="umJogoFoiAtualizado" class="d-flex justify-end"/>
    <v-responsive class="d-flex align-center text-center fill-height">
        <game-list @mudouStatus="actualizeTimer" />
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
  },
  data (){
    return{
      umJogoFoiAtualizado: 0
    }
  },
  methods: {
    actualizeTimer(){
      this.umJogoFoiAtualizado++
    }
  }
}
</script>
