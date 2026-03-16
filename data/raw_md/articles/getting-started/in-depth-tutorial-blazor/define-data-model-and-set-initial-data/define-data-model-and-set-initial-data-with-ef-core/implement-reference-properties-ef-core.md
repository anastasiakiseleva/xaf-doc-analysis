---
uid: "402978"
title: Implement Reference Properties
owner: Alexey Kazakov
seealso:
  - linkId: "112570"
  - linkId: "112571"
  - linkId: "112847"
  - linkId: "112701"
---
# Implement Reference Properties

This lesson explains the following concepts:

- How to implement object references to existing classes.
- How XAF generates a UI for referenced classes.

> [!NOTE]
> Before you proceed, take a moment to review the previous lesson:
> 
> * [](xref:402984)

## Step-by-Step Instructions

1. In the _MySolution.Module\Business Objects_ folder, create the `Position` class. Replace the generated class declaration with the following code:
    
    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using System.ComponentModel;

    namespace MySolution.Module.BusinessObjects {
        [DefaultClassOptions]
        [DefaultProperty(nameof(Title))]
        public class Position : BaseObject {
            public virtual string Title { get; set; }
        }
    }

    ```
    [`DefaultProperty`]: xref:System.ComponentModel.DefaultPropertyAttribute

2. Go to the _MySolution.Module\MySolutionDbContext_ file and add a DbSet of `Position` type:

    ```csharp
    public class MySolutionEFCoreDbContext : DbContext {
        //...
        public DbSet<Position> Positions { get; set; } 
    }
    
    ``` 

3. Add the `Position` property to the `Employee` class:

    ```csharp
    //...
    using System.Collections.ObjectModel;

    namespace MySolution.Module.BusinessObjects;

    [DefaultClassOptions]
    public class Employee : BaseObject {
        //...
        public virtual Position Position { get; set; }
    }
    ```

    The `Employee` class now exposes the `Position` reference property. This way, you effectively create a ["One-to-Many"](xref:402984) relationship between these entity classes.

4. Run the application. 

   You can see that the navigation control displays the **Position** item. Click this item to access the `Position` List View. Click **New** to open the `Position` Detail View.
   
5. Create **Developer** and **Manager** positions. They now appear in the `Position` List View:

   ASP.NET Core Blazor
 
   :   ![|ASP.NET Core Blazor list view|](~/images/btutor_bmd_custom_position_list.png)

   Windows Forms

   :   ![|Windows Forms list view|](~/images/position-listview-winforms.png)

6. Open the **Employee** Detail View. In this view, XAF creates a [lookup editor](xref:113572#lookuppropertyeditor) for the `Position` reference property. 

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor detail view lookup editor|](~/images/btutor_bmdef_contact_detail_view.png)

   Windows Forms

   :   ![|Windows Forms detail view lookup editor|](~/images/employee-detailview-position-winforms.png)

## Exercise: Add an "Address" Reference Property

1. Use the same steps to add an `Address` reference property to the `Employee` entity. You can find the type declaration in the code sample below.

   > [!TIP]
   >
   > Remember to register the new entity in `DbContext` and add a new property to the `Employee` class.

   ```csharp
   using DevExpress.Persistent.Base;
   using DevExpress.Persistent.BaseImpl.EF;
   using System.ComponentModel;

   namespace MySolution.Module.BusinessObjects;

   [DefaultProperty(nameof(FullAddress))]
   public class Address : BaseObject {
       private const string defaultFullAddressFormat = "{Country}; {StateProvince}; {City}; {Street}; {ZipPostal}";

       public virtual String Street { get; set; }

       public virtual String City { get; set; }

       public virtual String StateProvince { get; set; }

       public virtual String ZipPostal { get; set; }

       public virtual String Country { get; set; }

       public String FullAddress {
           get { return ObjectFormatter.Format(defaultFullAddressFormat, this, EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty); }
       }
   }
   ```

   This class is not visible in the navigation control, but you can create objects of this type from the reference property lookup editor.

2. Run the application and open the **Employee** Detail View. It should now contain the `Address` field:

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor Address reference property|](~/images/tutorial-address-lookup-editor-blazor.png)

   Windows Forms

   :   ![Windows Forms Address reference property](~/images/tutorial-address-lookup-editor-winforms.png)

## Next Lesson

[](xref:402982)
