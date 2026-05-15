---
uid: DevExpress.ExpressApp.Utils.ImageLoader.CustomGetImageInfo
name: CustomGetImageInfo
type: Event
summary: Occurs before image metadata is loaded.
syntax:
  content: public static event EventHandler<CustomGetImageInfoEventArgs> CustomGetImageInfo
seealso: []
---
Handle the `CustomGetImageInfo` event to supply an [](xref:DevExpress.ExpressApp.Utils.ImageInfo) object for a requested image. Use the [ImageName](xref:DevExpress.ExpressApp.Utils.CustomizeImageInfoEventArgs.ImageName) value to identify the image to load. The following example loads images from a database.

* Implement the following `MyImageObject` business class:
    
    # [C# (EF Core)](#tab/tabid-csharp-ef)

    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    // ...
    [DefaultClassOptions]
    public class MyImageObject : BaseObject {
        public virtual string Name { get; set; }
        [ImageEditorAttribute(ImageEditorMode.PictureEdit, ImageEditorMode.PictureEdit, 
            DetailViewImageEditorFixedHeight = 32, DetailViewImageEditorFixedWidth = 32)]
        [VisibleInListView(true)]
        public virtual byte[] Image { get; set; }
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)
    
    ```csharp
    using DevExpress.ExpressApp.DC;
    using DevExpress.ExpressApp.Model;
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.Xpo;
    using System.ComponentModel;
    //...
        [DefaultClassOptions]

        public class MyImageObject : XPObject {
        public MyImageObject(Session session) : base(session) { }

        string name;

        [Size(SizeAttribute.DefaultStringMappingFieldSize)]
        public string Name {
            get => name;
            set => SetPropertyValue(nameof(Name), ref name, value);
        }
        byte[] image;
        [ImageEditorAttribute(ImageEditorMode.PictureEdit, ImageEditorMode.PictureEdit,
                DetailViewImageEditorFixedHeight = 32, DetailViewImageEditorFixedWidth = 32)]
        [VisibleInListView(true)]
        [Size(SizeAttribute.Unlimited)]
        public byte[] Image { get => image; set => SetPropertyValue(nameof(Image), ref image, value); }
    }
    ```
    ***
  
* Create predefined **`MyImageObject` instances in the overridden [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method.
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();
        MyImageObject image1 = ObjectSpace.CreateObject<MyImageObject>();
        image1.Name = "Image 1";
        var stream = new System.IO.MemoryStream();
        ImageLoader.Instance.GetSmallImageInfo("Action_Save").Image.Save(stream, ImageFormat.Png);
        image1.Image = stream.ToArray();
    
        MyImageObject image2 = ObjectSpace.CreateObject<MyImageObject>();
        image2.Name = "Image 2";
        stream = new System.IO.MemoryStream();
        ImageLoader.Instance.GetSmallImageInfo("Action_Delete").Image.Save(stream, ImageFormat.Png);
        image2.Image = stream.ToArray();
        ObjectSpace.CommitChanges();
     }
    ```
        
    # [VB.NET](#tab/tabid-vb)
    
    ```vb
    Public Overrides Sub UpdateDatabaseAfterUpdateSchema()
        MyBase.UpdateDatabaseAfterUpdateSchema()
        Dim image1 As MyImageObject = ObjectSpace.CreateObject(Of MyImageObject)()
        image1.Name = "Image 1"
        Dim stream = New System.IO.MemoryStream()
        ImageLoader.Instance.GetSmallImageInfo("Action_Save").Image.Save(stream, ImageFormat.Png)
        image1.Image = stream.ToArray()
    
        Dim image2 As MyImageObject = ObjectSpace.CreateObject(Of MyImageObject)()
        image2.Name = "Image 2"
        stream = New System.IO.MemoryStream()
        ImageLoader.Instance.GetSmallImageInfo("Action_Delete").Image.Save(stream, ImageFormat.Png)
        image2.Image = stream.ToArray()
        ObjectSpace.CommitChanges()
    End Sub
    ```
    
    ***
* Edit the _Program.cs_ file and handle the static `CustomGetImageInfo` event before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called.
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using System.IO;
    using System.Drawing;
    using System.Drawing.Imaging;
    // ...
    ImageLoader.CustomGetImageInfo += (sender, e) => {
        if(e.ImageName.StartsWith(MyWindowController.MyImagePrefix)) {
            int key;
            string key_string = e.ImageName.Split('_')[1];
            if(int.TryParse(key_string, out key)) {
                using(IObjectSpace objectSpace = winApplication.CreateObjectSpace(typeof(MyImageObject))) {
                    MyImageObject imageObject = objectSpace.GetObjectByKey<MyImageObject>(key);
                    if(imageObject != null) {
                        e.ImageInfo = new ImageInfo(e.ImageName, Image.FromStream(new MemoryStream(imageObject.Image)), null);
                        e.Handled = true;
                    }
                }
            }
        }
    };
    ```
    
    # [VB.NET](#tab/tabid-vb)
    
    ```vb
    Imports System.IO
    Imports System.Drawing
    Imports System.Drawing.Imaging
    Imports DevExpress.ExpressApp.Web.Editors.ASPx
    ' ...
    Private ImageLoader.CustomGetImageInfo += Sub(s, args)
        If args.ImageName.StartsWith(MyWindowController.MyImagePrefix) Then
            Dim key As Integer
            Dim key_string As String = args.ImageName.Split("_"c)(1)
            If Integer.TryParse(key_string, key) Then
                Using objectSpace As IObjectSpace = WebApplication.Instance.CreateObjectSpace(GetType(MyImageObject))
                    Dim imageObject As MyImageObject = objectSpace.GetObjectByKey(Of MyImageObject)(key)
                    If imageObject IsNot Nothing Then
                        args.ImageInfo = New ImageInfo(args.ImageName, Image.FromStream(New MemoryStream(imageObject.Image)), _
                        ImageProcessorsHelper.GetImageUrl(objectSpace, imageObject, "Image"))
                        args.Handled = True
                    End If
                End Using
            End If
        End If
    End Sub
    ```
    
    ***

* Now, you can specify images as follows:
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    // ...
    public class MyWindowController : WindowController {
        public const string MyImagePrefix = "MyImageObject_";
        SingleChoiceAction action;
        public MyWindowController() : base() {
            this.TargetWindowType = WindowType.Main;
            action = new SingleChoiceAction(this, "My Action", DevExpress.Persistent.Base.PredefinedCategory.Edit);
            action.ImageMode = ImageMode.UseItemImage;
            action.ItemType = SingleChoiceActionItemType.ItemIsOperation;
        }
        protected override void OnActivated() {
            base.OnActivated();
            action.Items.Clear();
            using(IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(MyImageObject))) {
                foreach(MyImageObject imageObject in objectSpace.GetObjects<MyImageObject>()) {
                    ChoiceActionItem item = new ChoiceActionItem();
                    item.Caption = imageObject.Name;
                    item.ImageName = MyImagePrefix + imageObject.ID;
                    action.Items.Add(item);
                }
            }
        }
    }
    ```
    
    # [VB.NET](#tab/tabid-vb)
    
    ```vb
    Imports DevExpress.ExpressApp
    Imports DevExpress.ExpressApp.Actions
    ' ...
    Public Class MyWindowController
        Inherits WindowController
        Public Const MyImagePrefix As String = "MyImageObject_"
        Private action As SingleChoiceAction
        Public Sub New()
            MyBase.New()
            Me.TargetWindowType = WindowType.Main
            action = New SingleChoiceAction(Me, "My Action", DevExpress.Persistent.Base.PredefinedCategory.Edit)
            action.ImageMode = ImageMode.UseItemImage
            action.ItemType = SingleChoiceActionItemType.ItemIsOperation
        End Sub
        Protected Overrides Sub OnActivated()
            MyBase.OnActivated()
            action.Items.Clear()
            Using objectSpace As IObjectSpace = Application.CreateObjectSpace(GetType(MyImageObject))
                For Each imageObject As MyImageObject In objectSpace.GetObjects(Of MyImageObject)()
                    Dim item As New ChoiceActionItem()
                    item.Caption = imageObject.Name
                    item.ImageName = MyImagePrefix & imageObject.ID
                    action.Items.Add(item)
                Next imageObject
            End Using
        End Sub
    End Class
    ```
    
    ***