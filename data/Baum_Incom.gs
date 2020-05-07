function createForm() {
        // create & name Form
        var item = "Beratungslotse - Follow Me! (Incom)";
        var form = FormApp.create(item).setTitle(item);
        // Page 1
        var Page1 = form.addPageBreakItem().setTitle("Thema");
        var item1 = form.addMultipleChoiceItem();
        // Page 2
        var Page2 = form.addPageBreakItem().setTitle("Prima!");
        var item2 = form.addMultipleChoiceItem();
        // Page 3
        var Page3 = form.addPageBreakItem().setTitle("Idee für Thema ");
        var item3 = form.addMultipleChoiceItem();
        // Page 4
        var Page4 = form.addPageBreakItem().setTitle("Betreuer*in");
        var item4 = form.addMultipleChoiceItem();
        // Page 5
        var Page5 = form.addPageBreakItem().setTitle("Checkliste, Webseite, ...");
        var item5 = form.addMultipleChoiceItem();
        // Page 6
        var Page6 = form.addPageBreakItem().setTitle("Beratung, Terminabfrage, Ticketsystem").setHelpText("Bitte geben Sie mir einen Termin zur Beratung. Oder ein Ticketsystem?");
        // Page 7
        var Page7 = form.addPageBreakItem().setTitle("Genaues Thema");
        var item7 = form.addMultipleChoiceItem();
        // end page
        var endPage = form.addPageBreakItem().setTitle("Bis bald!").setHelpText("Hoffentlich konnte ich dir helfen!");
        item1.setTitle("Hast du ein genaues Thema?").setChoices([item1.createChoice('Ja', Page4), item1.createChoice('Nein', Page3)]).setRequired(true);
        item2.setTitle("Prima! Falls du noch weitere Angebote sehen möchtest, klicke bitte auf weiter.").setChoices([item2.createChoice('Weiter', Page6)]).setRequired(true);
        item3.setTitle("Hast du eine Idee für ein Thema?").setChoices([item3.createChoice('ja', Page4), item3.createChoice('nein', Page6)]).setRequired(true);
        item4.setTitle("Hast du einen Betreuer*in und ein genaues Thema?").setChoices([item4.createChoice('Ich habe ein*e Betreuer*in und ein Thema', Page2), item4.createChoice('Ich habe ein*e Betreuer*in, aber kein Thema', Page7), item4.createChoice('Nein', Page5)]).setRequired(true);
        item5.setTitle("Hast du alles erledigt? (Checkliste)").setChoices([item5.createChoice('Ja', Page7), item5.createChoice('Nein', Page6)]).setRequired(true);
        item7.setTitle("Triff dich mit mit deinem*r Betreuer*in. Konntest du dann ein genaues Thema formulieren?").setChoices([item7.createChoice('Ja', Page2), item7.createChoice('Nein', Page6)]).setRequired(true);
        Page6.setGoToPage(FormApp.PageNavigationType.SUBMIT);
        endPage.setGoToPage(FormApp.PageNavigationType.SUBMIT);
}