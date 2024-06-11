"""Admin for Clubs App."""

from django.contrib import admin

from apps.utils.admin import BaseAdmin
from .models import Club, ClubMember, Event, Topic, Discussion


@admin.register(Club)
class ClubAdmin(BaseAdmin):
    """Admin for Club model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["name", "members", "is_public", "is_available"]
    list_filter = ["is_available", "is_public", "category"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]


@admin.register(ClubMember)
class ClubMemberAdmin(BaseAdmin):
    """Admin for ClubMember model."""

    ordering = ["-created_at"]
    search_fields = ["club_id", "user_id"]
    list_display = ["club_id", "user_id", "is_available"]
    list_filter = ["is_available", "club_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Event)
class EventAdmin(BaseAdmin):
    """Admin for Event model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["club_id", "name", "is_available"]
    list_filter = ["is_available", "club_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Topic)
class TopicAdmin(BaseAdmin):
    """Admin for Topic model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["club_id", "is_available"]
    list_filter = ["is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Discussion)
class DiscussionAdmin(BaseAdmin):
    """Admin for Discussion model."""

    ordering = ["-created_at"]
    search_fields = ["topic_id"]
    list_display = ["topic_id", "content", "is_available"]
    list_filter = ["is_available", "topic_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
