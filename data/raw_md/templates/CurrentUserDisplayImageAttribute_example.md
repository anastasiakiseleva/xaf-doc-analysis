You can pass the name of a property that stores a user image to the [CurrentUserDisplayImage](xref:DevExpress.Persistent.Base.CurrentUserDisplayImageAttribute) attribute to display this image in the application toolbar.

Follow the steps below to extend a user class with a property that stores a user image:

1. In a user business class, declare a property of the `MediaDataObject` ([XPO](xref:DevExpress.Persistent.BaseImpl.MediaDataObject)/[EF Core](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject)), @System.Drawing.Image, or `byte[]` type.
2. Apply `CurrentUserDisplayImageAttribute` to the user class and pass the new property name as its parameter.

    **XPO**

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl;
    // ...
    [CurrentUserDisplayImage(nameof(Photo))]
    public class MyAppUser : PermissionPolicyUser, IObjectSpaceLink, ISecurityUserWithLoginInfo {
        // ...
        private MediaDataObject photo;
        public MediaDataObject Photo {
            get { return photo; }
            set { SetPropertyValue(nameof(Photo), ref photo, value); }
        }
    }
    ```
    ***

    **EF Core**

    # [C#](#tab/tabid-csharp-1)

    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl;
    // ...
    [CurrentUserDisplayImage(nameof(Photo))]
    public class MyAppUser : PermissionPolicyUser, IObjectSpaceLink, ISecurityUserWithLoginInfo {
        // ...
        private MediaDataObject photo;
        public virtual MediaDataObject Photo {
            get { return photo; }
            set { SetReferencePropertyValue(ref photo, value); }
        }
    }
    ```
    ***

