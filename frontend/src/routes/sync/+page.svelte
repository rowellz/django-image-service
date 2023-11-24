<script lang="ts">
  import { onMount } from 'svelte';
  import axios from 'axios';

  let file: File | null = null;
  let gif: Blob | null = null;
  let loading = false;
  let uploadProgress = 0;
  let matchedFilename = "";
  let textFromAudio = "";
  
  const handleFileChange = (event: any) => {
    file = event.target.files[0];
    if (file) {
      // (event.target as HTMLInputElement).style.backgroundImage = `url(${URL.createObjectURL(file)})`;
    }
  };
  
  const handleSubmit = async (event: any) => {
    if (!file) {
      return;
    }
    gif = null;

    loading = true;
    // (event.target as HTMLInputElement).style.backgroundImage = 'upload.jpeg';
    const formData = new FormData();
    formData.append('audio_file', file);
    formData.append('auto_text', textFromAudio? false : true);
    formData.append('text', textFromAudio);
    // formData.append('fps', fps[0].toString());
    // formData.append('min', imageDistortionMinMax[0].toString());
    // formData.append('max', imageDistortionMinMax[1].toString());
  
    try {
      const response = await axios.post('http://localhost:8000/my-force-aligner/', formData, {
        responseType: 'blob',
        onUploadProgress: event => {
        uploadProgress = (event.loaded / event.total) * 100;
      }
      });
      gif = response.data;
      const contentDisposition = response.headers['content-disposition'];
      const filenameMatch = contentDisposition && contentDisposition.match(/filename="(.+)"/);
      const filename = filenameMatch && filenameMatch[1];
      const matchResult = filename?.match(/(.+)\.webm/);
      matchedFilename = matchResult ? matchResult[1] : '';
      console.log(matchedFilename);
      console.log(response, response.config, response.data.filename);
      file = file;
    } catch (error) {
      console.error(error);
    }
    
    loading = false;
  };
  
  </script>
  
  <style>
    form {
      display: grid;
      flex-direction: column;
      align-items: center;
    }
  
    /* input[type="file"] {
      margin: 20px;
      border: dashed;
      cursor: pointer;
      background-image: url('./upload2.png');
      background-color: white;
      background-size: 100% 100%;
      height: 800px;
    }

    input[type="file"]::-webkit-file-upload-button {
      visibility: hidden;
      display: none;
    } */

    progress {
      justify-self: center;
      width: 50%;
      height: 40px;
      border-radius: 50px;
      background-color: #ddd;
    }

    progress::-webkit-progress-bar {
      border-radius: 50px;
      background-color: #ddd;
    }

    progress::-webkit-progress-value {
      border-radius: 50px;
      background-color: #4caf50;
    }

    button {
      border-top: 100px;
      height: 50px;
      font-size: 25px;
    }

    .container {
      border: dashed;
      justify-content: center;
    }

    #gif {
      min-height: 400px;
      max-height: 700px;
    }

    #gif-div {
      display: flex;
      justify-content: center;
    }

    @media (max-width: 700px) {
      #parent {
        width: 500px;
      }
    }

    .iframe {
      width: 100%;
      min-height: 500px;
      height: 100%;
      border: none;
    }
  </style>

  <div id="parent">
    <form on:submit={handleSubmit}>
      {#if loading}
        <progress value={uploadProgress} max="100"><div>{uploadProgress}%</div></progress>
        {:else}
          <input id="fileInput" type="file" on:change={handleFileChange} class:loading={loading}/> 
          <textarea id="textArea" bind:value={textFromAudio}></textarea>
          <button id="submit" type="submit" disabled={loading}>Generate GIF</button>
      {/if}
    </form>
      {#if gif}
        <video width= "320" height="240" controls>
          <source src={URL.createObjectURL(gif)} type="video/webm">
        </video>

        <iframe class="iframe" title="blah" src={"http://localhost:8003/transcriptions//" + matchedFilename}></iframe>
      {/if}
  </div>
  