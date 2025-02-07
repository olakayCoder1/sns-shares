from celery import shared_task
import logging
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from db_schema.models import ScheduleVideo, SocialConfig
from utils.socials.youtube import YouTubeManager
from utils.socials.instagram import InstagramMediaManager

logger = logging.getLogger(__name__)


@shared_task
def backgroud_upload(t_time):
    print(f"SCHEDULE TASK CALLED {t_time} :::: {datetime.now()}")



# @shared_task
# def schedule_for_background_upload(title,description,user_id,processing_id,choices):
#     social_configs = SocialConfig.objects.filter(provider__in=choices,added_by__id=user_id)
#     print(f"RECORDS :: {social_configs}")
#     try:
#         # print(social_configs)
#         videos = ScheduleVideo.objects.filter(processing_id=processing_id)
#         print(videos)
#         for video in videos:
#             for social in social_configs:
#                 for social in social_configs:
#                     if social.provider== "YOUTUBE":
#                         try:
#                             status_code, message, response = YouTubeManager.upload_video(
#                                 social_config=social,
#                                 video_file=video.file,
#                                 title=title,
#                                 description=description
#                             )
#                             video.delete()
#                         except Exception as e:
#                             print(e)
#                     elif social.provider == "INSTAGRAM":
#                         try:
#                             instagram_manager = InstagramMediaManager(
#                                 instagram_business_account_id=social.instagram_busiess_id,
#                                 access_token=social.facebook_access_token
#                             )
#                             res = instagram_manager.handle_video_upload(video_url=video.file.url,caption=title)
#                             if res.get("error"):
#                                 pass
#                             else:
#                                 video.delete()
#                         except Exception as e:
#                             print(e)
#                             pass
#                 print(f"SCHEDULE TASK PROCESSED {social.provider}")
            
#     except Exception as e:
#         print(e)




# Configure logging

@shared_task
def schedule_for_background_upload(title, description, user_id, processing_id, choices):
    try:
        # Fetch social configurations and log the count
        social_configs = SocialConfig.objects.filter(provider__in=choices, added_by__id=user_id)
        logger.info(f"Fetched {social_configs.count()} social_configs for user_id {user_id}")

        # Fetch videos for processing and log the count
        videos = ScheduleVideo.objects.filter(processing_id=processing_id)
        logger.info(f"Fetched {videos.count()} videos for processing_id {processing_id}")

        
        providers_map = {
            "YOUTUBE": YouTubeManager,
            "INSTAGRAM": InstagramMediaManager
        }

        for video in videos:
            for social in social_configs:
                provider_manager = providers_map.get(social.provider)
                
                if not provider_manager:
                    logger.warning(f"No manager found for provider {social.provider}")
                    continue

                try:
                    if social.provider == "YOUTUBE":
                        status_code, message, response = provider_manager.upload_video(
                            social_config=social,
                            video_file=video.file,
                            title=title,
                            description=description
                        )
                    elif social.provider == "INSTAGRAM":
                        instagram_manager = provider_manager(
                            instagram_business_account_id=social.instagram_business_id,
                            access_token=social.facebook_access_token
                        )
                        res = instagram_manager.handle_video_upload(video_url=video.file.url, caption=title)
                        if res.get("error"):
                            logger.error(f"Instagram upload error: {res.get('error')}")
                            continue
                        
                    video.delete()
                    logger.info(f"Successfully processed and deleted video {video.id} for provider {social.provider}")
                    
                except Exception as e:
                    logger.error(f"Error processing video {video.id} for provider {social.provider}: {e}")

    except ObjectDoesNotExist as e:
        logger.error(f"Object does not exist: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
