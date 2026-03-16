---
uid: DevExpress.Persistent.Base.ImageEditorAttribute
name: ImageEditorAttribute
type: Class
summary: Applied to business class properties of the byte array type. Specifies that the target property persists an image. Attribute parameters specify settings to be used by [Image Property Editors](xref:113544) when displaying images persisted by the target property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true, AllowMultiple = false)]
    public class ImageEditorAttribute : ModelExportedValuesAttribute
seealso:
- linkId: DevExpress.Persistent.Base.ImageEditorAttribute._members
  altText: ImageEditorAttribute Members
---
By default, `byte[]` properties are displayed via Default Property Editor as a collection of bytes. If the `ImageEditorAttribute` attribute is applied, [Image Property Editors](xref:113544) are used. These Property Editors are instantiated using default settings when the `ImageEditorAttribute` attribute is applied without parameters. However, it is often necessary to specify different settings for the Property Editors that display images represented by different properties. To do this, pass the settings as the parameters. This will make all the Image Property Editors use the specified settings when displaying images.

Basically, there are two groups of settings - the settings that affect the Image Property Editors used in [Detail Views](xref:112611) and the settings that affect the inplace Image Property Editors used in [List Views](xref:112611). The following table lists the `ImageEditorAttribute` class' public properties that can be passed as named parameters in the attribute's constructor:

| Name | Description |
|---|---|
| [ImageEditorAttribute.DetailViewImageEditorFixedHeight](xref:DevExpress.Persistent.Base.ImageEditorAttribute.DetailViewImageEditorFixedHeight) | Specifies the fixed height of Image Property Editors in Detail Views. |
| [ImageEditorAttribute.DetailViewImageEditorFixedWidth](xref:DevExpress.Persistent.Base.ImageEditorAttribute.DetailViewImageEditorFixedWidth) | Specifies the fixed width of Image Property Editors in Detail Views. |
| [ImageEditorAttribute.DetailViewImageEditorMode](xref:DevExpress.Persistent.Base.ImageEditorAttribute.DetailViewImageEditorMode) | Specifies how images represented by the target Image property must be displayed in WinForms Detail Views. |
| [ImageEditorAttribute.ImageSizeMode](xref:DevExpress.Persistent.Base.ImageEditorAttribute.ImageSizeMode) | Specifies how images represented by the target Image property must be resized in WinForms Image Property Editor. |
| [ImageEditorAttribute.ListViewImageEditorCustomHeight](xref:DevExpress.Persistent.Base.ImageEditorAttribute.ListViewImageEditorCustomHeight) | Specifies the height of inplace Image Property Editors in List Views. |
| [ImageEditorAttribute.ListViewImageEditorMode](xref:DevExpress.Persistent.Base.ImageEditorAttribute.ListViewImageEditorMode) | Specifies how images represented by the target Image property must be displayed in WinForms List Views. |

These parameters have the corresponding properties in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelMember) node. When the `ImageEditorAttribute` is applied to a property, the parameter's values are assigned to the Application Model's property of the node that represents the target property. These Application Model properties values, in turn, are set to the relative properties of the [](xref:DevExpress.ExpressApp.Model.IModelColumn) and [](xref:DevExpress.ExpressApp.Model.IModelPropertyEditor) nodes that also correspond to the target property.

The following code snippets demonstrate the `ImageEditorAttribute` usage.

* All the Property Editors that represent the `Photo` property will display images in drop-down windows:
    
    # [C# (EF Core)](#tab/tabid-csharp-ef)

    ```csharp
    using System.Drawing;  
    //...
    public class Contact : BaseObject {
        //...        
        [ImageEditor(ListViewImageEditorMode = ImageEditorMode.DropDownPictureEdit, 
            DetailViewImageEditorMode = ImageEditorMode.DropDownPictureEdit)]
        public virtual byte[] Photo { get; set; }
        //...
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)
    
    ```csharp
    using System.Drawing;
    using DevExpress.Persistent.Base;
    
    //...
    
    public class Contact : BaseObject {
    //...
            
        [ImageEditor(ListViewImageEditorMode = ImageEditorMode.DropDownPictureEdit, 
            DetailViewImageEditorMode = ImageEditorMode.DropDownPictureEdit)]
        public byte[] Photo {
            get { return GetPropertyValue<byte[]>(nameof(Photo)); }
            set { SetPropertyValue<byte[]>(nameof(Photo), value); }
        }
    
    //...
    }
    ```
    ***
* All the Property Editors that represent the `Photo` property in Detail Views will have a fixed width of 40 pixels :
    
    # [C# (EF Core)](#tab/tabid-csharp-ef)

    ```csharp
    using System.Drawing;
    //...
    public class Contact : BaseObject {
        //...
    
        [ImageEditor(DetailViewImageEditorMode = ImageEditorMode.PictureEdit, 
            DetailViewImageEditorFixedWidth = 40)]
        public virtual byte[] Photo { get; set; }
        //...
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)
    
    ```csharp
    using System.Drawing;
    using DevExpress.Persistent.Base;
    //...
    public class Contact : BaseObject {
    //...
    
        [ImageEditor(DetailViewImageEditorMode = ImageEditorMode.PictureEdit, 
            DetailViewImageEditorFixedWidth = 40)]
        public byte[] Photo {
            get { return GetPropertyValue<byte[]>(nameof(Photo)); }
            set { SetPropertyValue<byte[]>(nameof(Photo), value); }
        }
    //...
    }
    ```
    ***