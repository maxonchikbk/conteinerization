## Лекция 1. Микросервисы и контейнеры

**Перед второй лекцией нужно установить Docker**

Вы можете [установить Docker](https://docs.docker.com/get-docker/) на свой компьютер или виртуальную машину с Linux.

А так же использовать онлайн сервисы, чтобы немедленно приступить к обучению:

🔹 [Play with Docker](https://labs.play-with-docker.com/)

🔹 [Katacoda](https://www.katacoda.com/)

**Паттерны проектирования**

🔹 [The Twelwe-Factor App](https://12factor.net/ru/)

🔹 [GRASP](https://ru.wikipedia.org/wiki/GRASP)

🔹 Рекомендую книгу - [Чистая архитектура. Искусство разработки программного обеспечения](https://www.piter.com/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya)

**Механизмы контейнеризации**

🔹 [Linux-контейнеры: изоляция как технологический прорыв](https://habr.com/ru/company/redhatrussia/blog/352052/)

🔹 [Namespaces](https://habr.com/ru/company/selectel/blog/279281/)

🔹 [Cgroups](https://habr.com/ru/company/selectel/blog/303190/)

🔹 [Capabilities](https://habr.com/ru/company/otus/blog/471802/)

🔹 [Могут ли контейнеры быть безопасными?](https://habr.com/ru/company/oleg-bunin/blog/480630/)

## Лекция 2. Docker

**Docker**

🔹 [Overview of Docker CLI](https://docs.docker.com/engine/reference/run/)

🔹 [10 команд для Docker, без которых вам не обойтись](https://tproger.ru/translations/top-10-docker-commands/)

🔹 [Как начать использовать Docker в своих проектах](https://tproger.ru/translations/how-to-start-using-docker/)

🔹 [50 вопросов по Docker, которые задают на собеседованиях, и ответы на них](https://habr.com/ru/company/southbridge/blog/528206/)

**Dockerfile**

🔹 [20 лучших практик по работе с Dockerfile](https://habr.com/ru/company/domclick/blog/546922/)

🔹 [ENTRYPOINT vs CMD: назад к основам](https://habr.com/ru/company/southbridge/blog/329138/)

🔹 [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

🔹 [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/)

🔹 [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy%23add-or-copy)

**Docker Compose**

🔹 [Overview of docker-compose CLI](https://docs.docker.com/compose/reference/)

🔹 [Quickstart: Compose and Django](https://docs.docker.com/samples/django/)

🔹 [Compose file version 3 reference](https://docs.docker.com/compose/compose-file/compose-file-v3/)

🔹 [Compose file version 2 reference](https://docs.docker.com/compose/compose-file/compose-file-v2/)

## Лекция 3. Введение в Kubernetes

>Уважаемые студенты, просьба по возможности до начала занятия поставить себе утилиту для работы с Kubernetes – kubectl.
>Это можно сделать по инструкциям из официальной документации для вашей ОС.
>https://kubernetes.io/docs/tasks/tools/install-kubectl/

Делаем работу с kubectl удобнее:

🔹 [kubectl auto-complition](https://kubernetes.io/docs/tasks/tools/included/optional-kubectl-configs-bash-linux/)

🔹 [kubectl aliases](https://github.com/adterskov/kubectl-aliases)

🔹 [kubens - быстрый способ переключения между namespaces в kubectl](https://github.com/ahmetb/kubectx/)

🔹 [kubecolor - раскрашивает вывод kubectl](https://github.com/dty1er/kubecolor/)

Как получить в своё распоряжение полноценный кластер Kubernetes?

**Онлайн сервисы, чтобы немедленно приступить к обучению**

🔹 [Play with Kubernetes](https://labs.play-with-k8s.com/)

🔹 [Katacoda](https://www.katacoda.com/)

**Запустить локальный кластер Kubernetes**

🔹 [Minikube](https://kubernetes.io/ru/docs/tasks/tools/install-minikube/)

🔹 [Minishift (OpenShift)](https://www.okd.io/minishift/)

🔹 [KiND](https://kind.sigs.k8s.io/docs/user/quick-start/)

🔹 [Docker Desktop](https://docs.docker.com/desktop/kubernetes/)

**Запустить кластер Kubernetes в облаке**

🔹 [Google Cloud Platform (300$ на счет за регистрацию)](https://cloud.google.com/free)

🔹 Российские облачные провайдеры Yandex и MCS (mail.ru) периодически дают бонусы на счет, например за прохождение вебинаров

**Установить кластер самостоятельно**

🔹 [Установка в помощью kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/)

🔹 [Установка с помощью kubesparay](https://kubernetes.io/docs/setup/production-environment/tools/kubespray/)
