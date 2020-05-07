function createForm() {
        
        // create & name Form
        var item = "Digitale Studienberatung";
        var form = FormApp.create(item).setTitle(item);
        // Page 1
        var Page1 = form.addPageBreakItem().setTitle("Herzlich Willkommen zur Online-Hausarbeitshilfe!");
        title = "Hast du ein genaues Thema?";
        var item = form.addMultipleChoiceItem();  
        item.setTitle(title).setChoices([item.createChoice('Ja', Page2), item.createChoice('Nein', Page3)]).setRequired(true);
        // Page 2
        var Page2 = form.addPageBreakItem().setTitle("You're on a good way!").setHelpText("Prima. ");
        // Page 3
        var Page3 = form.addPageBreakItem().setTitle("You‘re on a bad way!").setHelpText("Schade.");
        
}