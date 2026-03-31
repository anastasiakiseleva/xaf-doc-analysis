---
uid: "404256"
title: Extend the Data Model
---
# Extend the Data Model

This lesson explains how to extend your entity class with different properties.

During this lesson, you will do the following:

- Add properties of different types to the entity class.
- See how the field editor type depends on the property's value type.

1. Add the following properties to the `Employee` class:

    ```csharp{2}
    //...
    using System.ComponentModel.DataAnnotations.Schema;

    namespace MySolution.Module.BusinessObjects;

    [DefaultClassOptions]
    public class Employee : BaseObject {
        //...

        public virtual DateTime? Birthday { get; set; }

        //Use this attribute to hide or show the editor of this property in the UI.
        [Browsable(false)]
        public virtual int TitleOfCourtesy_Int { get; set; }

        //Use this attribute to exclude the property from database mapping.
        [NotMapped]
        public virtual TitleOfCourtesy TitleOfCourtesy { get; set; }
        
    }

    public enum TitleOfCourtesy {
        Dr,
        Miss,
        Mr,
        Mrs,
        Ms
    }
    ```

    The `NotMapped` attribute requires the [](xref:System.ComponentModel.DataAnnotations.Schema) using directive.

2. Run the application and invoke the `Employee` object's Detail View. The application displays a date picker for the `DateTime` type of values (see **Birthday**) and a combo box for the enumeration fields (see **Title Of Courtesy**):

   ASP.NET Core Blazor
        
   :   ![|XAF ASP.NET Core Blazor Field Editors|](~/images/tutorial-field-editors-blazor.gif)
   
   Windows Forms

   :   ![|XAF Windows Forms App List View|](~/images/tutorial-field-editors-winforms.gif)    

3. Extend the `Employee` class further with the following properties. Note the attributes that decorate these properties. Use hyperlinks to learn more about the attributes if their meanings are not immediately clear.

   ```csharp{9,10}
   //...
   using DevExpress.Persistent.Validation;
   using System.ComponentModel.DataAnnotations;

   namespace MySolution.Module.BusinessObjects;

   [DefaultClassOptions]
   //Use this attribute to specify the caption format for the objects of the entity class.
   [ObjectCaptionFormat("{0:FullName}")]   
   [DefaultProperty(nameof(FullName))]
   public class Employee : BaseObject {
       //...

       [SearchMemberOptions(SearchMemberMode.Exclude)]
       public String FullName {
           get { return ObjectFormatter.Format(FullNameFormat, this, EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty); }
       }

       [EditorBrowsable(EditorBrowsableState.Never)]
       public String DisplayName {
           get { return FullName; }
       }

       public static String FullNameFormat = "{FirstName} {MiddleName} {LastName}";

       //Use this attribute to specify the maximum number of characters that users can type in the editor of this property.
       [FieldSize(255)]
       public virtual String Email { get; set; }

       //Use this attribute to define a pattern that the property value must match.
       [RuleRegularExpression(@"(((http|https)\://)[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(:[a-zA-Z0-9]*)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;amp;%\$#\=~])*)|([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})", CustomMessageTemplate = @"Invalid ""Web Page Address"".")]
       public virtual string WebPageAddress { get; set; }

       //Use this attribute to specify the maximum string length allowed for this data field.
       [StringLength(4096)]
       public virtual string Notes { get; set; }

    }
    ```
    [`RuleRegularExpression`]: xref:DevExpress.Persistent.Validation.RuleRegularExpressionAttribute
    [`StringLength`]: xref:System.ComponentModel.DataAnnotations.StringLengthAttribute
    [`NotMapped`]: xref:System.ComponentModel.DataAnnotations.Schema.NotMappedAttribute
    [`FieldSize`]: xref:DevExpress.ExpressApp.DC.FieldSizeAttribute
    [`SearchMemberOptions`]: xref:DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute
    [`ObjectCaptionFormat`]: xref:DevExpress.Persistent.Base.ObjectCaptionFormatAttribute

4. Run the application and invoke the `Employee` object's Detail View:

   ASP.NET Core Blazor

   :   ![|XAF ASP.NET Core Blazor Employee|](~/images/employee-final-iteration-blazor.png)

   Windows Forms:

   :   ![XAF WinForms Employee](~/images/employee-final-iteration-winforms.png)

   As you can see, XAF places the **Notes** editor outside of the group box that contains smaller editors. This is the framework's default behavior for user-resizable editors. If you want to change the layout, use the steps described in the following lesson: [](xref:403217).

## Next Lesson

[](xref:402985)