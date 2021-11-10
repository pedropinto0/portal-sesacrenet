from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """title and text and nothing else"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichTextBlock(blocks.RichTextBlock):
  class Meta:
      template = "streams/richtext_block.html"
      icon = "edit"
      label = "Full RichText"

class CardBlock(blocks.StructBlock):
   title = blocks.CharBlock(required=True, help_text="Add your title") 

   cards = blocks.ListBlock(
       blocks.StructBlock(
           [
               ("image", ImageChooserBlock(required=True)),
               ("title", blocks.CharBlock(required=True, max_length=40)),
               ("text", blocks.TextBlock(required=True, max_length=300)),
               ("button_page", blocks.PageChooserBlock(required=False)),
               ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first")),
           ]
       )   
   )
   class Meta:
      template = "streams/card_block.html"
      icon = "placeholder"
      label = "Staff Cards"

class CTABlock(blocks.StructBlock):
    """A simple call to action selections."""
    title = blocks.CharBlock(required=False, max_length=60)
    text = blocks.RichTextBlock(required=True,)
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)   
    button_text = blocks.CharBlock(required=True, default="learn more", max_length=50)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"

class LinkStructValue(blocks.StructValue):
    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None
        
    # def latest_posts(self):
    #     return BlogDetailPage.objects.live()[:3]

class ButtonBlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required=False, help_text='Se selecionado, esse URL será usado primeiro')
    button_url = blocks.URLBlock(required=False, help_text='Se adicionado, esse URL será usado secundariamente')

    # def get_context(self, request, **args, **kwargs):
    #         context = super().get_context(request, **args, **kwargs)
    #         context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
    #         return context


    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue
