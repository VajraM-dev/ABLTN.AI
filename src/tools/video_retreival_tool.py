from langchain.tools import tool
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat

@tool
def retrieve_transcripts(video_urls: list[str]):
    """
    This function retrieves transcripts for a list of YouTube video URLs.
    Args:
        video_urls (list[str]): A list of YouTube video URLs.
    Returns:
        str: Concatenated transcripts of the provided videos.
    """

    transcripts = ""

    try:
        for video in video_urls[:3]:

            loader = YoutubeLoader.from_youtube_url(
                video,
                add_video_info=False,
                transcript_format=TranscriptFormat.CHUNKS,
                chunk_size_seconds=30,
            )

            transcripts += "\n\n".join(map(repr, loader.load()))

        return transcripts
    except ValueError as e:
        return "Failed to retrieve transcripts continue with next one"
    except Exception as e:
        return f"An error occurred: {str(e)}"