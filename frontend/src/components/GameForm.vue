<template>
  <div>
    <v-list-item prepend-icon="mdi-nintendo-game-boy" color="green" title="Add game" @click="showPopup"></v-list-item>
    <v-dialog v-model="showForm" max-width="500px" @click:outside="cleanForm">
      <v-card class="pa-5">
        <v-card-title class="headline">Add Game</v-card-title>
        <v-card-text>
          <v-form ref="form" v-model="valid">
            <v-text-field v-model="title" prepend-icon="mdi-format-title" label="Title" :rules="titleRules" />
            <v-text-field v-model="platform" prepend-icon="mdi-laptop" label="Platform" :rules="platformRules" />
            <v-text-field v-model="gameCover" prepend-icon="mdi-image-area"
              label="Cover (copy img adress w/ right mouse click)" type="url" :rules="imageRules" />
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="green" @click="submit">Submit</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import { ref } from 'vue'
import { useAppStore } from "@/stores/appStore"
import gamesApi from "@/api/games.api.js"
import eventBus from '@/api/eventBus.js';


export default {
  setup() {
    const form = ref(null)
    const showForm = ref(false)
    const valid = ref(false)
    const title = ref('')
    const platform = ref('')
    const gameCover = ref('')
    const appStore = useAppStore()

    const titleRules = [
      v => !!v || 'Title is required',
      v => (v && v.length <= 25) || 'Title must be less than 25 characters'
    ]
    const platformRules = [
      v => !!v || 'Artist is required',
      v => (v && v.length <= 25) || 'Artist must be less than 25 characters'
    ]
    const imageRules = [
      v => !!v || 'Game cover is required',
    ]

    function showPopup() {
      showForm.value = true
    }
    async function submit() {
      if (valid.value) {
        const newGame = {
          title: title.value,
          platform: platform.value,
          cover: gameCover.value,
        }

        await gamesApi.addNewgame(newGame)
        showForm.value = false
        cleanForm()

        eventBus.emit('gameAdded');
      }
      else {
        form.value.validate()
      }
    }
    function cleanForm() {
      form.value.reset()
    }

    return {
      appStore,
      showForm,
      form,
      valid,
      title,
      platform,
      gameCover,
      titleRules,
      platformRules,
      imageRules,
      showPopup,
      submit,
      cleanForm,
    }
  }
}
</script>