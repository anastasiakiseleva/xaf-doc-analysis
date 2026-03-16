---
uid: DevExpress.ExpressApp.Utils.ImageLoader.ImageInfoLoading
name: ImageInfoLoading
type: Event
summary: Occurs when an image is loading. Set the **Cancel** event argument to **true** to skip loading.
syntax:
  content: public event EventHandler<ImageInfoLoadingEventArgs> ImageInfoLoading
seealso: []
---
For example, you can handle this event if **ImageLoader** cannot find an image, but you do not want to write the following message to the log file in [Verbose (4) mode](xref:112575#change-the-log-file-detail-level):  
"_ImageLoader: Image is not found by its name in the following sources..._".
