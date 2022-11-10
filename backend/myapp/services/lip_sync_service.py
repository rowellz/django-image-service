from afaligner import align





class LipSyncService:
    def sync_audio_and_text(audio, text):

        sync_map = align(
            'ebooks/demoebook/text/',
            'ebooks/demoebook/audio/',
            output_dir='ebooks/demoebook/smil/',
            output_format='smil',
            sync_map_text_path_prefix='../text/',
            sync_map_audio_path_prefix='../audio/'
        )
