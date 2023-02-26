<template>
  <div>
    <v-container class="mt-5"> 
        <h1 class="text-h5 font-weight-bold mb-3">Fila</h1>
        <v-col
           v-for="(game, index) in gameRow"
          :key="index"
          cols="12"
        >
        <v-hover>
         <template #default="{ isHovering, props }">
          <v-card
            v-bind="props"
            dark
            height="90"
            rounded
          >
          <div class="d-flex flex-no-wrap justify-start">
            <v-card-actions>
                <v-btn
                  v-if="isHovering"
                  icon="mdi-play"
                  height="40px"
                  right
                  width="40px"
                >
                </v-btn>
                <span v-else class="mx-4 text-body">{{ index+1 }}</span>
              </v-card-actions>
              <v-avatar
                class="ma-3"
                size="70"
                rounded="0"
              >
                <v-img :src="game.cover"></v-img>
              </v-avatar>
              <div>
                <v-card-title
                  class="text-h5"
                >
                  {{ game.title }}
                </v-card-title>

                <v-card-subtitle>{{  game.platform }}</v-card-subtitle>
              </div>
            </div>
          </v-card>
        </template>
  </v-hover>
        </v-col>
    </v-container>
    
  </div>
</template>

<script setup>
import { useGameStore } from "@/stores/gameStore"
import { mapState } from "pinia"
</script>

<script>
export default {
    computed: {
    ...mapState(useGameStore, ["gameRow"]),
  },
}
</script>

<style>

</style>