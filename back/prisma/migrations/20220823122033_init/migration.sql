-- CreateEnum
CREATE TYPE "Role" AS ENUM ('INDIVIDUAL', 'COMPANY');

-- CreateEnum
CREATE TYPE "Discipline" AS ENUM ('Discipline1');

-- CreateEnum
CREATE TYPE "Skills" AS ENUM ('Skills1');

-- CreateEnum
CREATE TYPE "WorkType" AS ENUM ('Work1');

-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "email" TEXT NOT NULL,
    "firstname" TEXT,
    "lastname" TEXT,
    "role" "Role" NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Individual" (
    "id" SERIAL NOT NULL,
    "userId" INTEGER NOT NULL,
    "languageId" INTEGER,
    "address" TEXT NOT NULL,
    "disciplines" "Discipline"[],
    "skills" "Skills"[],
    "galop" INTEGER,
    "maxMoveKm" INTEGER,
    "selfEmployed" BOOLEAN NOT NULL,
    "searchingWork" BOOLEAN NOT NULL,
    "workType" "WorkType"[],
    "workTime" TEXT,
    "experience" INTEGER,
    "prices" JSONB NOT NULL,
    "housingNeed" BOOLEAN NOT NULL,
    "profilPicture" TEXT,
    "professionnalCard" TEXT,
    "license" TEXT,
    "rate" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "Individual_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Language" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "flag" TEXT,

    CONSTRAINT "Language_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Individual_userId_key" ON "Individual"("userId");

-- CreateIndex
CREATE UNIQUE INDEX "Language_name_key" ON "Language"("name");

-- AddForeignKey
ALTER TABLE "Individual" ADD CONSTRAINT "Individual_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Individual" ADD CONSTRAINT "Individual_languageId_fkey" FOREIGN KEY ("languageId") REFERENCES "Language"("id") ON DELETE SET NULL ON UPDATE CASCADE;
