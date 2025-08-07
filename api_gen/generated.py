from openapi_client.api.default_api import DefaultApi


class IconikAPI:
    """
     This class was generated using the SimpleApiGenerator.
    """

    def __init__(self, app_id: str, auth_token: str) -> None:
        self.api = DefaultApi()
        self.app_id = app_id
        self.auth_token = auth_token

    def bulk_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_approvals_bulk_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def bulk_remove_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_approvals_bulk_remove_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def get_asset(
        self,
        *args,
        **kwargs
    ) -> Asset:
        return Asset(
            self.api.v1_assets_asset_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def history_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_history_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def history_history_entity_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_history_history_entity_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def history_history_entity_id_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_history_history_entity_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def history_history_entity_id_reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_history_history_entity_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def history_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_history_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def edit(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def purge_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_purge_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def set(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relations_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_relations_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relations_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_relations_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relations_relation_type_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_relations_relation_type_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relations_relation_type_related_to_asset_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_relations_relation_type_related_to_asset_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relations_relation_type_related_to_asset_id_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_relations_relation_type_related_to_asset_id_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relations_relation_type_related_to_asset_id_reverse_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_relations_relation_type_related_to_asset_id_reverse_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def restore_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_restore_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def search_document_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_search_document_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_bulk_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_bulk_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_bulk_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_bulk_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_bulk_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_bulk_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_csv_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_csv_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_segment_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_segment_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_segment_id_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_segment_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_segment_id_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_segment_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_segment_id_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_segment_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_segment_id_reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_segment_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_segment_type_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_segment_type_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_srt_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_srt_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_vtt_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_segments_vtt_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def shares_all_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_shares_all_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def uploads_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_uploads_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_from_assets_source_asset_id_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_from_assets_source_asset_id_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_from_versions_source_version_id_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_from_versions_source_version_id_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_old_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_old_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_promote_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_promote_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_transcriptions_properties_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_transcriptions_properties_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_transcriptions_properties_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_transcriptions_properties_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_transcriptions_subtitles_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_transcriptions_subtitles_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_transcriptions_transcription_id_properties_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_transcriptions_transcription_id_properties_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_transcriptions_transcription_id_properties_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_transcriptions_transcription_id_properties_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_transcriptions_transcription_id_properties_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_transcriptions_transcription_id_properties_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def versions_version_id_transcriptions_transcription_id_properties_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_versions_version_id_transcriptions_transcription_id_properties_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def views_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_asset_id_views_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def asset_get_list(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def asset_bulk_edit(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def asset_create(
        self,
        *args,
        **kwargs
    ) -> Asset:
        return Asset(
            self.api.v1_assets_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def asset_bulk_set(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relation_types_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_relation_types_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relation_types_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_relation_types_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relation_types_relation_type_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_relation_types_relation_type_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relation_types_relation_type_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_relation_types_relation_type_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relation_types_relation_type_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_relation_types_relation_type_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def relation_types_relation_type_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_relation_types_relation_type_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_assets_segments_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def ancestors_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_ancestors_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def content_info_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_content_info_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def contents_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_contents_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def contents_object_type_object_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_contents_object_type_object_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def contents_object_type_object_id_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_contents_object_type_object_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def contents_object_type_object_id_reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_contents_object_type_object_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def contents_ordering_custom_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_contents_ordering_custom_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def contents_ordering_custom_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_contents_ordering_custom_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def contents_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_contents_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def full_path_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_full_path_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def get_collection(
        self,
        *args,
        **kwargs
    ) -> Collection:
        return Collection(
            self.api.v1_collections_collection_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def keyframes_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_keyframes_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def edit(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def purge_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_purge_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def set(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_contents_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_reindex_contents_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def restore_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_restore_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def search_document_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_search_document_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def size_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_size_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def subcollections_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_collection_id_subcollections_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def collection_get_list(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def collection_create(
        self,
        *args,
        **kwargs
    ) -> Collection:
        return Collection(
            self.api.v1_collections_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_collections_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def context_action_id_callback_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_context_action_id_callback_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def context_action_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_context_action_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def context_action_id_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_context_action_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def context_action_id_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_context_action_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def context_action_id_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_context_action_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def context_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_context_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def context_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_context_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def custom_action_get_list(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def shared_context_action_id_callback_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_custom_actions_shared_context_action_id_callback_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_assets_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_assets_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_assets_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_assets_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_assets_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_assets_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_assets_purge_all_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_assets_purge_all_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_assets_purge_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_assets_purge_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_assets_restore_all_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_assets_restore_all_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_bulk_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_bulk_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_collections_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_collections_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_collections_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_collections_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_collections_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_collections_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_collections_purge_all_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_collections_purge_all_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_collections_purge_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_collections_purge_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_collections_restore_all_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_collections_restore_all_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete_queue_purge_all_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_delete_queue_purge_all_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def favorites_all_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_favorites_all_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def favorites_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_favorites_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def favorites_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_favorites_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def favorites_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_favorites_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def favourites_all_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_favourites_all_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_external_email_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_external_email_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_request_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_request_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_request_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_request_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_request_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_request_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_request_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_request_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_request_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_request_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_approvals_user_user_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_approvals_user_user_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_users_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_users_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_users_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_users_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_users_share_user_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_users_share_user_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_users_share_user_id_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_users_share_user_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_users_share_user_id_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_users_share_user_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_share_id_users_share_user_id_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_share_id_users_share_user_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_shares_url_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_shares_url_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_versions_version_id_approvals_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_versions_version_id_approvals_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def object_type_object_id_versions_version_id_approvals_request_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_object_type_object_id_versions_version_id_approvals_request_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def persons_person_id_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_persons_person_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def playlist_get_list(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def get_playlist(
        self,
        *args,
        **kwargs
    ) -> Playlist:
        return Playlist(
            self.api.v1_playlists_playlist_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def items_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_items_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_item_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_items_item_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_item_id_patch(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_items_item_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_item_id_position_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_items_item_id_position_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_item_id_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_items_item_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_items_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def edit(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def set(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_playlists_playlist_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def playlist_create(
        self,
        *args,
        **kwargs
    ) -> Playlist:
        return Playlist(
            self.api.v1_playlists_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def project_get_list(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def project_create(
        self,
        *args,
        **kwargs
    ) -> Project:
        return Project(
            self.api.v1_projects_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def get_project(
        self,
        *args,
        **kwargs
    ) -> Project:
        return Project(
            self.api.v1_projects_project_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def members_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_members_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def members_member_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_members_member_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def members_member_id_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_members_member_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def members_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_members_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def edit(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def set(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_projects_project_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_bulk_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_reindex_bulk_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def segments_reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_segments_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def sequence_get_list(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def sequence_create(
        self,
        *args,
        **kwargs
    ) -> Sequence:
        return Sequence(
            self.api.v1_sequences_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def get_sequence(
        self,
        *args,
        **kwargs
    ) -> Sequence:
        return Sequence(
            self.api.v1_sequences_sequence_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def items_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_items_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_item_id_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_items_item_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_item_id_position_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_items_item_id_position_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def items_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_items_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def edit(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def set(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def reindex_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sequences_sequence_id_reindex_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def share_object_type_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_share_object_type_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def all_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_shares_all_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def auth_login_post(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_shares_auth_login_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def auth_token_get(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_shares_auth_token_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def auth_token_put(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_shares_auth_token_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def bulk_all_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_shares_bulk_all_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def bulk_delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_shares_bulk_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def share_get_list(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_shares_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def sync_session_create(
        self,
        *args,
        **kwargs
    ) -> Sync_session:
        return Sync_session(
            self.api.v1_sync_sessions_post(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def delete(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sync_sessions_sync_session_id_delete(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def get_sync_session(
        self,
        *args,
        **kwargs
    ) -> Sync_session:
        return Sync_session(
            self.api.v1_sync_sessions_sync_session_id_get(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)
        )

    def edit(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sync_sessions_sync_session_id_patch(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

    def set(
        self,
        *args,
        **kwargs
    ) -> any:
        return self.api.v1_sync_sessions_sync_session_id_put(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)

